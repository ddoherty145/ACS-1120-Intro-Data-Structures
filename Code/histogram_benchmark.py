import timeit
from dictogram import Dictogram
from listogram import Listogram
from hashtable import HashTable

# Sample text (8000 words)
words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'] * 1000  

# Create histograms
dictogram = Dictogram(words)
listogram = Listogram(words)

# Create HashTable with a large bucket size
hashtable = HashTable(init_size=1024)

# Populate HashTable
for word in words:
    try:
        count = hashtable.get(word)
    except KeyError:
        count = 0
    hashtable.set(word, count + 1)

# Benchmark function
def benchmark_count(hist, word):
    if hasattr(hist, 'frequency'):  # For Dictogram and Listogram
        return timeit.timeit(lambda: hist.frequency(word), number=10000)
    else:  # For HashTable
        return timeit.timeit(lambda: hist.get(word) if hist.contains(word) else 0, number=10000)

# Run benchmark
search_word = 'fish'
print(f"Listogram: (O(n)): {benchmark_count(listogram, search_word)} seconds")
print(f"Dictogram: (O(1)): {benchmark_count(dictogram, search_word)} seconds")
print(f"HashTable: (O(1)): {benchmark_count(hashtable, search_word)} seconds")