import json

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    all_words = load_json('words_list.json')
    letters_points = load_json('letters.json')

    scores = {}

    # Convert all words to uppercase to handle lowercase and uppercase uniformly
    all_words = [word.upper() for word in all_words]

    for word in all_words:
        score = 0
        for i, l in enumerate(word, 1):
            # Convert the letter to uppercase in case it's lowercase
            score += letters_points[l.upper()][str(i)]
        scores[word] = score

    save_to_json(scores, "words_scores.json")

if __name__ == "__main__":
    main()
