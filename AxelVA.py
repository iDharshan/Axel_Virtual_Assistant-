import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except sr.UnknownValueError:
        print("I could'nt get it.")
    except:
        pass
    return command

def hello():
    talk("I am Axel. What can i do for you")

hello()

def run_axel():


    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H %M %p')
        talk('Current time is' + time)
    elif 'what is meant by' in command:
        meaning = command.replace('what is meant by', '')
        info = wikipedia.summary(meaning, 1)
        print(info)
        talk(info)

    elif 'who is' in command:
        person = command.replace('who is', '')
        inform = wikipedia.summary(person, 1)
        print(inform)
        talk(inform)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'twitter' in command:
        talk("Opening Twitter")
        webbrowser.open("https://twitter.com/home")
    elif 'instagram' in command:
        talk("Opening Instagram")
        webbrowser.open("https://www.instagram.com/")
    elif 'anime' in command:
        talk("Opening Anime")
        webbrowser.open("https://www.animekisa.vip/")
    elif 'stop' in command:
        talk("Bye bye")
        exit()
    elif 'tell me your name' in command:
        talk("I Am Axel, Darshan's Virtual assistant")


while True:
   run_axel()



