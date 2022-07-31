from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        command = request.form["sample"]
        command = {'command': command}
        print(command)
        requests.post('https://0647-49-37-156-187.in.ngrok.io/', command)
        return ''


if __name__ == "__main__":
    app.run()
