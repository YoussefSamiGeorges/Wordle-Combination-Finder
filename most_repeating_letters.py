import json
import string


def load_words(file_path):
    # Load words from JSON and convert them to uppercase
    with open(file_path, 'r') as f:
        return [word.upper() for word in json.load(f)]  # Convert all words to uppercase


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def create_alphabet_position_dict():
    alphabet = string.ascii_uppercase
    position_dict = {letter: {pos: 0 for pos in range(1, 6)} for letter in alphabet}
    return position_dict


def main():
    all_words = load_words('wordle_words.json')
    alphabet_dict = create_alphabet_position_dict()

    # Iterate over all words and count occurrences of letters in each position
    for word in all_words:
        for i, l in enumerate(word, 1):
            if l in alphabet_dict:
                alphabet_dict[l][i] += 1

    # Display the dictionary
    for l, n in alphabet_dict.items():
        print(l, ":", n)

    save_to_json(alphabet_dict, "letters.json")


if __name__ == "__main__":
    main()
