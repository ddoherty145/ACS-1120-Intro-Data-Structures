import random
import string 
from dictogram import Dictogram

class MarkovChain:
    """Generates text using a Markov chain."""
    def __init__(self, text):
        """Initialize the Markov chain."""
        self.chain = {} # dictionary to store word transitions
        words = self.clean_and_tokenize(text)

        # populate the markov chian using a dictogram
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]

            if current_word not in self.chain:
                self.chain[current_word] = Dictogram() # using dictogram to track next word frequency
            self.chain[current_word].add_count(next_word)

    def clean_and_tokenize(self, text):
        """Clean text and split into words."""
        text = text.translate(str.maketrans("", "", string.punctuation))
        return text.split()
    
    def generate_sentence(self, length=10):
        """Generate a sentence of a given length."""
        if not self.chain:
            return "No words available."
        
        # choose a random startinf word
        current_word = random.choice(list(self.chain.keys()))
        sentence = [current_word]

        for _ in range(length -1):
            next_words = self.chain.get(current_word)
            if not next_words:
                break
            current_word = next_words.sample()
            sentence.append(current_word)

        return " ".join(sentence)
    
if __name__ == "__main__":
    text = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!"
    markov = MarkovChain(text)
    print(markov.generate_sentence(15))
