from flask import Flask, render_template, jsonify, request, session
from markov import MarkovChain
import random

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required for session management

# Load the text files as corpora
with open("Code/data/corpus.txt", "r", encoding="utf-8") as file:
    corpus = file.read()

with open("Code/data/sample.txt", "r", encoding="utf-8") as file:
    sample = file.read()

# Initialize Markov Chains for both corpora
markov_corpus = MarkovChain(corpus)
markov_sample = MarkovChain(sample)

@app.route("/")
def home():
    """Generate and return a random sentence."""
    # Randomly select a corpus
    selected_corpus = random.choice(["corpus", "sample"])
    if selected_corpus == "corpus":
        sentence = markov_corpus.generate_sentence(15)
    else:
        sentence = markov_sample.generate_sentence(15)

    # Store the selected corpus in the session
    session["selected_corpus"] = selected_corpus

    # Initialize score if it doesn't exist
    if "score" not in session:
        session["score"] = 0

    return render_template("index.html", sentence=sentence, score=session["score"])

@app.route("/generate")
def generate():
    """Generate and return a random sentence as JSON."""
    # Randomly select a corpus
    selected_corpus = random.choice(["corpus", "sample"])
    if selected_corpus == "corpus":
        sentence = markov_corpus.generate_sentence(15)
    else:
        sentence = markov_sample.generate_sentence(15)

    # Store the selected corpus in the session
    session["selected_corpus"] = selected_corpus

    return jsonify({"sentence": sentence, "selected_corpus": selected_corpus})

@app.route("/guess", methods=["POST"])
def guess():
    """Handle user guesses and update the score."""
    user_guess = request.json.get("guess")
    selected_corpus = session.get("selected_corpus")

    if user_guess == selected_corpus:
        session["score"] += 1
        result = "Correct!"
    else:
        result = "Incorrect!"

    return jsonify({"result": result, "score": session["score"]})

@app.route("/reset", methods=["POST"])
def reset():
    """Reset the score to 0."""
    session["score"] = 0
    return jsonify({"score": session["score"]})

if __name__ == "__main__":
    app.run(debug=True)