import wikipedia
from flask import Flask
from flask import request
from variables import *

app = Flask(__name__)

text = ''


@app.route("/")
def showHomePage():
	return "This is home page"

@app.route("/debug", methods=["POST", "GET"])
def debug():
    if request.method == 'POST':
        command = request.form["sample"]
        print(command)
        command = [command.lower()]
        command = convert(command)
        print(2, command)
        if command[0] == "what" or command[0] == "who":
            command = list_to_string(command)
            command = wikipedia.summary(command, sentences=3)
            speak_text(command)
            print(command)
        elif command[0] == "open" and command[1] == "youtube":
            print("yt")
            speak_text("opening YouTube")
            command.remove('open')
            command = list_to_string(command)
            website(command)
        
        elif command[0] == "open" and len(command) < 3:
            speak_text("opening")
            speak_text(command[1])
            command.remove("open")
            command = list_to_string(command)
            open_app(command)
        elif command == ['play', 'my', 'music']:
            speak_text("Playing your music")
            my_music()
        elif command[0] == "play":
            command.remove("play")
            command = list_to_string(command)
            music_yt(command)
        elif command[0] == "open" and command[2] == "website":
            speak_text("Opening ")
            speak_text(command[1])
            command.remove("open")
            command.remove('website')
            command = list_to_string(command)
            website(command)
        else:
            print("internal else")
    else:
        print("else")
        pass
    
    return ''
    
	

if __name__ == "__main__":
    app.run(port=80)
