import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

# Function to respond to commands
def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        today = datetime.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "search" in command:
        speak("What would you like to search for?")
        query = recognize_speech()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the results for {query}")
    else:
        speak("Sorry, I can't help with that.")

# Main function
def main():
    speak("How can I assist you?")
    while True:
        command = recognize_speech()
        if command:
            respond_to_command(command)
        else:
            speak("Please repeat your command.")

if __name__ == "__main__":
    main()
