from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "service": "flask-demo"}), 200


@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify(
        {"message": "Hello from Flask!", "items": ["item1", "item2", "item3"]}
    ), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
