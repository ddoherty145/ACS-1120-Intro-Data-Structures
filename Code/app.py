from flask import Flask, render_template, jsonify
from markov import MarkovChain

app = Flask(__name__)

# Load the text file as a corpus
with open("Code/data/corpus.txt", "r", encoding="utf-8") as file:
    corpus = file.read()

# Initialize the Markov Chain
markov_chain = MarkovChain(corpus)

@app.route("/")
def home():
    """Generate and return a random sentence."""
    sentence = markov_chain.generate_sentence(15)
    return render_template("index.html", sentence=sentence)

@app.route("/generate")
def generate():
    """Generate and return a random sentence as JSON."""
    sentence = markov_chain.generate_sentence(15)
    return jsonify({"sentence": sentence})

if __name__ == "__main__":
    app.run(debug=True)