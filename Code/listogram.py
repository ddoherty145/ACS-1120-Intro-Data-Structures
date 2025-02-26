import random

class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super().__init__()  # Initialize as an empty list
        self.types = 0  # Count of distinct word types
        self.tokens = 0  # Total count of all word tokens

        if word_list:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase count of given word, or add it if not found."""
        index = self.index_of(word)

        if index is not None:  # Word found, update count
            old_word, old_count = self[index]
            self[index] = (old_word, old_count + count)
        else:  # Word not found, add new word
            self.append((word, count))
            self.types += 1  # Increase distinct word count

        self.tokens += count  # Update total token count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if not found."""
        index = self.index_of(word)
        return self[index][1] if index is not None else 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        return self.index_of(word) is not None

    def index_of(self, target):
        """Return the index of entry containing given target word, or None."""
        for index, (word, count) in enumerate(self):
            if word == target:
                return index
        return None

    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting."""
        words, weights = zip(*self)  # Unpack words and weights
        return random.choices(words, weights=weights, k=1)[0]  # Weighted choice

    def __repr__(self):
        """Return a string representation of this histogram."""
        return f"Listogram({self})"
