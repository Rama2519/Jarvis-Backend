from flask import Flask, jsonify

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def main():
	command = "Who is Jimmy Carter"
	json_file = {'query': command}
	return jsonify(command)

if __name__ == "__main__":
	app.run()
