from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        request_data = request.data  # getting the response data
        request_data = json.loads(request_data.decode('utf-8'))  # converting it from json to key value pair
        command = [request_data['sample']]
        command = {'command': command}
        print(command)
        requests.post('https://f7df-49-37-159-104.in.ngrok.io/', command)
        return ''


if __name__ == "__main__":
    app.run()
