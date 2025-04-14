import json
from multiprocessing import Pool, cpu_count


def load_words(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def filter_word(word):
    return len(word) == len(set(word))


def process_chunk(chunk):
    return [word for word in chunk if filter_word(word)]


def main():
    all_words = load_words('all_words.json')

    # Determine optimal chunk size
    chunk_size = max(1, len(all_words) // (cpu_count() * 4))

    # Create chunks of words
    chunks = [all_words[i:i + chunk_size] for i in range(0, len(all_words), chunk_size)]

    # Set up the pool with the number of available CPUs
    with Pool(cpu_count()) as pool:
        # Process chunks in parallel
        results = pool.map(process_chunk, chunks)

    # Flatten the results
    out_word_list = [word for chunk in results for word in chunk]
    print(len(out_word_list))
    with open("words_list.json", 'w') as f:
        json.dump(out_word_list, f)


if __name__ == "__main__":
    main()
