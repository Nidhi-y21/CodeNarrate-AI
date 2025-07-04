### CodeNarrate AI - Minimal Working MVP
# Structure: tracer, narrator (Azure OpenAI), speaker (Azure TTS), runner

# === app/tracer.py ===
import sys

class CodeTracer:
    def __init__(self):
        self.trace_log = []

    def trace_lines(self, frame, event, arg):
        if event == "line":
            lineno = frame.f_lineno
            code = frame.f_globals["__file__"]
            line = open(code).readlines()[lineno - 1].strip()
            self.trace_log.append((lineno, line))
        return self.trace_lines

    def run_code(self, filepath):
        with open(filepath) as f:
            code = f.read()
        sys.settrace(self.trace_lines)
        exec(code, {"__file__": filepath})
        sys.settrace(None)
        return self.trace_log

# === app/narrator.py ===
import openai
import os

openai.api_key = os.getenv("AZURE_OPENAI_KEY")

class Narrator:
    def narrate(self, line):
        prompt = f"Explain in simple terms what this Python line does:\n{line}"
        response = openai.ChatCompletion.create(
            engine="gpt-4",  # Replace with your Azure OpenAI deployment name
            messages=[
                {"role": "system", "content": "You are an AI code explainer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=50
        )
        return response.choices[0].message.content.strip()

# === app/speaker.py ===
import os
import azure.cognitiveservices.speech as speechsdk

speech_key = os.getenv("AZURE_SPEECH_KEY")
service_region = os.getenv("AZURE_SPEECH_REGION")

class Speaker:
    def __init__(self):
        self.speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    def speak(self, text):
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config)
        synthesizer.speak_text_async(text)

# === app/runner.py ===
from tracer import CodeTracer
from narrator import Narrator
from speaker import Speaker
import sys

if __name__ == "__main__":
    script_path = sys.argv[1] if len(sys.argv) > 1 else "test_scripts/sample.py"
    
    tracer = CodeTracer()
    narrator = Narrator()
    speaker = Speaker()

    print(f"Running: {script_path}\n")
    log = tracer.run_code(script_path)

    for lineno, line in log:
        explanation = narrator.narrate(line)
        print(f"Line {lineno}: {line}\nExplanation: {explanation}\n")
        speaker.speak(explanation)

# === test_scripts/sample.py ===
# Create this as a simple test script
name = "World"
print("Hello, " + name)

# === .env.example ===
# Rename to .env and fill with your actual keys
AZURE_OPENAI_KEY=your_openai_key
AZURE_SPEECH_KEY=your_speech_key
AZURE_SPEECH_REGION=your_region
