import os
from bs4 import BeautifulSoup
import json


def scrape_local_files(directory):
    all_words = []
    black_words = []
    red_words = []
    green_words = []

    # Iterate through all HTML files in the directory
    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.html'):
            file_path = os.path.join(directory, filename)
            print(f"Scraping file: {filename}")

            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')

                # Find all <span> tags with class "mt"
                word_spans = soup.find_all('span', class_='mt')

                for span in word_spans:
                    # Process words in red
                    red_spans = span.find_all('span', class_='rd')
                    for red_span in red_spans:
                        words = red_span.text.split()
                        for word in words:
                            if word.isupper() and len(word) == 5:
                                all_words.append(word)
                                red_words.append(word)

                    # Process words in green
                    green_spans = span.find_all('span', class_='gn')
                    for green_span in green_spans:
                        words = green_span.text.split()
                        for word in words:
                            if word.isupper() and len(word) == 5:
                                all_words.append(word)
                                green_words.append(word)

                    # Process black words (words directly in the "mt" span, not in "rd" or "gn" spans)
                    for word in span.contents:
                        if isinstance(word, str):
                            words = word.split()
                            for w in words:
                                if w.isupper() and len(w) == 5:
                                    all_words.append(w)
                                    black_words.append(w)

    return all_words, black_words, red_words, green_words


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    # Replace this with the path to your directory containing the HTML files
    local_directory = r"C:\programming\projectes\wordle_finder\web"

    all_words, black_words, red_words, green_words = scrape_local_files(local_directory)

    save_to_json(all_words, "all_words.json")
    save_to_json(black_words, "black_words.json")
    save_to_json(red_words, "red_words.json")
    save_to_json(green_words, "green_words.json")

    print(f"Total words scraped: {len(all_words)}")
    print(f"Black words scraped: {len(black_words)}")
    print(f"Red words scraped: {len(red_words)}")
    print(f"Green words scraped: {len(green_words)}")
    print("Data saved to all_words.json, black_words.json, red_words.json, and green_words.json")