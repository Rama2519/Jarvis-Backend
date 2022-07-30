from flask import Flask, jsonify, request

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		command = requesst.form["sample"]
		command = {'command': command}
		return jsonify(command)
	else:
		command = "Not complete yet"
		command = {'command': command}
		return jsonify(command)

if __name__ == "__main__":
	app.run()
