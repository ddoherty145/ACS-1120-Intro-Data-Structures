import sys
import string
import random
from collections import Counter

def histogram(source_text):
    if isinstance(source_text, str):  # Check if input is a string
        try:
            with open(source_text, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Error: The file '{source_text}' was not found.")
            sys.exit(1)
    else:
        text = source_text

    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = text.split()
    return Counter(words)

def random_word(histogram):
    """Select a single word at random from the histogram (uniform distribution)"""
    return random.choice(list(histogram.keys()))

def random_words_weighted(histogram):
    """Select a single word at random, weighted by frequency"""
    words = list(histogram.keys())
    weights = list(histogram.values())  # Fixed `.value()` to `.values()`
    return random.choices(words, weights=weights, k=1)[0]  # Use `random.choices()`

def unique_words(histogram):
    """Returns the number of unique words in the histogram"""
    return len(histogram)

def frequency(word, histogram):
    """Returns the frequency of a word in the histogram"""
    return histogram.get(word.lower(), 0)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 histogram.py <text_file>")
        sys.exit(1)

    text_file = sys.argv[1]
    
    # Generate Histogram
    word_histogram = histogram(text_file)

    # Get unique word count
    unique_count = unique_words(word_histogram)

    print(f"Total Unique Words: {unique_count}")

    # Print a random word (uniform)
    print("Random Word (Uniform):", random_word(word_histogram))

    # Print a random word (weighted)
    print("Random Word (Weighted by frequency):", random_words_weighted(word_histogram))

if __name__ == "__main__":
    main()
