from flask import Flask
import random
from markov import MarkovChain

app = Flask(__name__)

# load the text file as a corpus
with open("Code/data/corpus.txt", "r", encoding="utf-8") as file:
    corpus = file.read()

markov_chain = MarkovChain(corpus)

@app.route("/")
def home():
    """Generate and Return a random sentence."""
    sentence = markov_chain.generate_sentence(15)
    return f"<h1>{sentence}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
