import random
import sys
import subprocess

def read_words_file(file_path):
    """Reads a file containing words and returns a list of words."""
    try:
        with open(file_path, 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)

def count_words_in_file(file_path):
    """Counts the number of lines in a file using the wc command."""
    try:
        result = subprocess.run(['wc', '-l', file_path], stdout=subprocess.PIPE, text=True)
        return int(result.stdout.split()[0])
    except Exception as e:
        print(f"Error counting words in file: {e}")
        sys.exit(1)

def generate_sentence(words, num_words):
    """Generates a random sentence with the requested number of words."""
    if num_words > len(words):
        print("Error: Requested number of words exceeds the number of available words.")
        sys.exit(1)
    return " ".join(random.sample(words, num_words))

def main():
    """Main function to handle user input and generate a sentence."""
    if len(sys.argv) != 2:
        print("Usage: python3 dictionary_words.py <number_of_words>")
        sys.exit(1)
    
    try:
        num_words = int(sys.argv[1])
    except ValueError:
        print("Error: The number of words must be an integer.")
        sys.exit(1)

    # Path to the words file
    words_file = '/usr/share/dict/words'

    # Count words in the file (optional, for debugging or validation)
    word_count = count_words_in_file(words_file)
    print(f"The word file contains {word_count} words.")

    # Read words from the file
    words = read_words_file(words_file)

    # Generate and print the sentence
    sentence = generate_sentence(words, num_words)
    print(f"Generated Sentence: {sentence}")

if __name__ == "__main__":
    main()
