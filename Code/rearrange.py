import random
import sys

def rearrange_words(words):
    random.shuffle(words)
    return words

def main():
    if len(sys.argv) < 2:
        print("Use: python rearrange.py word1 word2 word3 ...")
        sys.exit(1)

    words = sys.argv[1:]
    rearranged = rearrange_words(words)

    print(" ".join(rearranged))

if __name__ == "__main__":
    main()