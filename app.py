from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
	"""Root route with basic info."""
	return (
		"<h1>Minimal Flask App</h1>"
		"<p>Available routes:</p>"
		"<ul>"
		"<li><a href=\"/hello/World\">/hello/&lt;name&gt;</a></li>"
		"<li><a href=\"/health\">/health</a></li>"
		"</ul>"
	)


@app.route("/hello/<name>", methods=["GET"])
def hello(name: str):
	"""Return a friendly greeting."""
	return jsonify({"message": f"Hello, {name}!"})


@app.route("/health", methods=["GET"])
def health():
	"""Simple health check endpoint."""
	return jsonify({"status": "ok"})


if __name__ == "__main__":
	# Runs with: python app.py
	app.run(host="0.0.0.0", port=5000, debug=True)

