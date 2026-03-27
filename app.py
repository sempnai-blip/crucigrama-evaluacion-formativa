from flask import Flask, render_template
from crossword import GRID

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", grid=GRID)

if __name__ == "__main__":
    app.run(debug=True)