import json
from itertools import permutations
import multiprocessing as mp


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.score = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, score):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
        current.score = score

    def find_combinations(self, words, num_words):
        result = []
        self._backtrack(words, [], set(), num_words, result, 0)
        return result

    def _backtrack(self, words, current_combo, current_chars, num_words, result, current_score):
        if len(current_combo) == num_words:
            result.append((current_combo.copy(), current_score))
            return

        for word, score in words.items():
            if not set(word) & current_chars:
                current_combo.append(word)
                current_chars.update(set(word))
                new_score = current_score + score

                self._backtrack(words, current_combo, current_chars, num_words, result, new_score)

                current_combo.pop()
                current_chars.difference_update(set(word))


def load_words(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def find_combinations_chunk(chunk, num_words):
    trie = Trie()
    for word, score in chunk.items():
        trie.insert(word, score)
    return trie.find_combinations(chunk, num_words)


def main():
    words = load_words('words_scores.json')
    num_words = 4
    num_processes = mp.cpu_count()

    # Split the words dictionary into chunks for multiprocessing
    chunk_size = len(words) // num_processes
    chunks = [{k: words[k] for k in list(words.keys())[i:i + chunk_size]} for i in range(0, len(words), chunk_size)]

    with mp.Pool(processes=num_processes) as pool:
        results = pool.starmap(find_combinations_chunk, [(chunk, num_words) for chunk in chunks])

    # Combine and sort results
    all_combinations = [item for sublist in results for item in sublist]
    all_combinations.sort(key=lambda x: x[1], reverse=True)

    # Get the top 10 combinations
    top_combination = all_combinations[0]

    print(f"Top combination with highest scores:")
    print(top_combination)



if __name__ == "__main__":
    main()
