import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    # it takes microphone input and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        speak("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        speak(f"sir you said: {query}\n")
        print(f"Command Taken: {query}\n")


    except Exception as e:
        #print(e)
        speak("Sorry sir I can't hear you...Please say that again ")
        return "None"
    return query
