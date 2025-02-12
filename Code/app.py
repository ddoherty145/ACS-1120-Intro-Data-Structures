"""Main script, uses other modules to generate sentences."""
from flask import Flask
from histogram import histogram, random_words_weighted


app = Flask(__name__)


word_histogram = histogram(".Code/data/corpus.txt")
# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

@app.route("/hello_world")
def hello_world():
    """Route that returns a simple string."""
    return "Hello, World!"

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    random_word = random_words_weighted(word_histogram)
    return f"<p>Random Word: {random_word}</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
