from flask import Flask, jsonify, request

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
async def main():
	if request.method == 'POST':
		command = await request.form["sample"]
		command = {'command': command}
		print(command)
		return jsonify(command)
     

if __name__ == "__main__":
	app.run()
