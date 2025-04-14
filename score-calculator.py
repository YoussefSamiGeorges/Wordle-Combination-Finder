import json


def calculate_combination_score(combination, word_scores):
    """
    Calculate the score of a given combination of words.
    
    Args:
        combination (list): A list of words to calculate the score for
        word_scores (dict): Dictionary mapping words to their scores
        
    Returns:
        int or float: The total score of the combination
        None: If the combination contains invalid words or overlapping characters
    """
    # Check if all words are in the word_scores dictionary
    for word in combination:
        if word not in word_scores:
            print(f"Warning: '{word}' not found in word scores dictionary")
            return None

    # Check for character overlap
    all_chars = set()
    for word in combination:
        word_chars = set(word)
        if word_chars & all_chars:  # If there's an intersection (overlap)
            print(f"Warning: Character overlap detected in combination {combination}")
            return None
        all_chars.update(word_chars)

    # Calculate the total score
    total_score = sum(word_scores[word] for word in combination)

    return total_score


def load_words(file_path):
    """
    Load word scores from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing word scores
        
    Returns:
        dict: Dictionary mapping words to their scores
    """
    with open(file_path, 'r') as f:
        return json.load(f)


def evaluate_combination(combination, file_path=None, word_scores=None):
    """
    Evaluate a specific word combination and return its score.
    
    Args:
        combination (list): List of words to evaluate
        file_path (str, optional): Path to word scores JSON file
        word_scores (dict, optional): Dictionary of word scores if already loaded
        
    Returns:
        int or float: The score of the combination
        None: If the combination is invalid
    """
    if word_scores is None:
        if file_path is None:
            raise ValueError("Either file_path or word_scores must be provided")
        word_scores = load_words(file_path)

    return calculate_combination_score(combination, word_scores)


if __name__ == "__main__":

    combination =["JUNKS", "WHOMP", "CALYX", "FRITZ"]

    word_scores = load_words('words_scores.json')
    score = calculate_combination_score(combination, word_scores)

    if score is not None:
        print(f"The combination {combination} has a score of {score}")
        print(f"Words: {', '.join(combination)}")
        print(f"Total Score: {score}")
    else:
        print("Invalid combination")
