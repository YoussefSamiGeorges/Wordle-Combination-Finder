import os
from bs4 import BeautifulSoup
import json


def scrape_html_file(file_path):
    all_words = []

    # Open and parse the HTML file using BeautifulSoup
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # Find all list items that contain the word links
        word_items = soup.find_all('a')

        # Iterate through all <a> tags and collect the words
        for item in word_items:
            word = item.text.strip()
            if len(word) == 5 and word.isalpha():  # Only add 5-letter alphabetic words
                all_words.append(word)

    return all_words


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    # Path to the uploaded HTML file
    file_path = r"Wordle Words - All 2309 Words (Not in Order) No Spoilers!.html"

    # Scrape the HTML file and get the list of all words
    all_words = scrape_html_file(file_path)

    # Save the list to a JSON file
    save_to_json(all_words, "wordle_words.json")

    print(f"Total words scraped: {len(all_words)}")
    print("Data saved to wordle_words.json")
