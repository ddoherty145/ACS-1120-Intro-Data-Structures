import sys
import string
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

def unique_words(histogram):
    """Returns the number of unique words in the histogram"""
    return len(histogram)

def frequency(word, histogram):
    """Returns the frequency of a word in the histogram"""
    return histogram.get(word.lower(), 0)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 histogram.py <text_file> <word1> <word2> ...")
        sys.exit(1)

    text_file = sys.argv[1]
    words_to_check = sys.argv[2:]  # Allow checking multiple words

    # Generate Histogram
    word_histogram = histogram(text_file)

    # Get unique word count
    unique_count = unique_words(word_histogram)

    print(f"Total Unique Words: {unique_count}")

    # Check frequency for each word provided
    for word in words_to_check:
        word_freq = frequency(word, word_histogram)
        print(f"Frequency of '{word}': {word_freq}")

if __name__ == "__main__":
    main()
