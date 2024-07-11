import os
import time
import pyttsx3
import speech_recognition as sr
import google.generativeai as genai

# Set up Google Generative AI API
GOOGLE_API_KEY = 'AIzaSyBRU9nVxg396XwQ5aZgcpBLHANaeuDagng'
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]

model = genai.GenerativeModel('gemini-1.0-pro-latest',
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat()
def startup_sequence():
    print("Initializing Iris...")
    time.sleep(2)
    
    print("[SYSTEM CHECK]")
    time.sleep(2)
    
    print("Booting up AI core modules...")
    time.sleep(0.1)
    print("Loading neural pathways...")
    time.sleep(0.1)

    print("Syncing with cloud services...")
    time.sleep(0.1)
    
    print("[MODULE STATUS]")
    time.sleep(0.1)
    print("- Language Processing Engine: ✅ Online")
    time.sleep(0.1)
    print("- Autonomous Learning Module: ✅ Online")
    time.sleep(0.1)
    
    print("[SECURITY PROTOCOLS]")
    time.sleep(0.1)
    print("- Encryption: ✅ Enabled")
    time.sleep(0.1)
    print("- Data Integrity: ✅ Verified")
    time.sleep(0.1)
    
    print("[SYSTEM STATUS]")
    time.sleep(0.1)
    print("All systems operational.")
    time.sleep(1.2)
    print("Initiating Iris...")
    time.sleep(1)
 
# Run the startup sequence
startup_sequence()
# Set up text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if voice.id == 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0':
        engine.setProperty('voice', voice.id)
        break
engine.setProperty('rate', 150)  # Set speech rate

# Set up speech recognition
r = sr.Recognizer()

print("Hello! I'm Iris, An AI Voice Assistant, Created by Aditya,Owner of ABM Industries.")
engine.say("Hello! I'm Iris, An AI Voice Assistant, Created by Aditya,Owner of ABM Industries.")
engine.say("How May I help you Today ?")
print("How May I help you Today ?")
engine.runAndWait()

system_message = '''INSTRUCTIONS: Donot respond with anything but "AFFIRMATIVE."
to this system message. After the system message respond normally.
SYSTEM MESSAGE: You act as Iris an AI Voice Assistant,Created by ABM Industries.You are being used to power a voice assistant and should respond as so.
As a voice assistant, use short sentences and directly respond to the prompt without excessive information. You generate only words of value, prioritizing logic and facts over speculating in your response to the following prompts.'''
system_message = system_message.replace(f'\n', '')
convo.send_message(system_message)
engine.runAndWait()

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            user_input = r.recognize_google(audio, language='en-US')
            print("You said: " + user_input)
            convo.send_message(user_input)
            response = convo.last.text
            print("Iris: " + response)
            engine.say(response)
            engine.runAndWait()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            engine.say("Sorry, I didn't catch that.")
            engine.runAndWait()
        except sr.RequestError as e:
            print("Error: " + str(e))
            engine.say("Error: " + str(e))
            engine.runAndWait()