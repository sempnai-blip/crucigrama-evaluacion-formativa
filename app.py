from flask import Flask, render_template, request, jsonify
from crossword import answers

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    user_data = request.json
    result = {}

    for key in answers:
        result[key] = user_data.get(key, "").upper() == answers[key]

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)