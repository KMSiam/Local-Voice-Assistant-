import speech_recognition as sr
import pyttsx3, datetime, pywhatkit,wikipedia, pyjokes, webbrowser, datetime, os

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower() 
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        talk("Sorry, I did not understand that.")
        command = ""
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        talk("Sorry, my speech service is down.")
        command = ""
    return command

def run_alexa():
    command = take_command()
    if command:
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk("Current time is " + time)
        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'tell me about' in command:
            look_for = command.replace('tall me about', '')
            info = wikipedia.summary(look_for, 1)
            print(info)
            talk(info)
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        elif 'open youtube' in command:
            print("Opening YouTube")
            talk("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in command:
            print("Opening Google")
            talk("Opening Google")
            webbrowser.open("https://www.google.com")
        elif 'open notepad' in command:
            print("Opening Notepad")
            talk("Opening Notepad")
            os.system("notepad.exe")
        elif 'quit' in command or 'exit' in command:
            print("Goodbye!")
            talk("Goodbye!")
            exit()
        else:
            print("I did not get it but I am going to search it for you")
            talk("I did not get it but I am going to search it for you")
            pywhatkit.search(command)


if __name__ == "__main__":
    print('Hello, how can I help you today?')
    talk("Hello, how can I help you today?")
    while True:
        run_alexa()