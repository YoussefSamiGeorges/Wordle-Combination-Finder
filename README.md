# Wordle Combination Finder

## Project Overview

This project finds optimal word combinations for the popular word game Wordle. By analyzing letter frequencies and their positions, this tool identifies the best set of words to use as initial guesses to maximize information gain and efficiently narrow down possible solutions.

The core strategy is to find combinations of words where:
1. Each word has no repeated letters
2. No letter is repeated across the entire combination
3. The selected words contain letters that frequently appear in their common positions in Wordle solutions

## Why This Matters

A good Wordle strategy involves using initial guesses that cover as many different letters as possible, with preference for common letters in their frequent positions. This project implements an algorithm to find the mathematically optimal combinations based on letter frequency analysis.

## Key Finding

My analysis determined that the optimal 4-word combination is:
```
['HOWFS', 'IXTLE', 'JUMBY', 'KRANG'] with a score of 2659
```

This outperforms the commonly cited combination `['JUNKS', 'WHOMP', 'CALYX', 'FRITZ']` which scores only 2464 according to my methodology.

## Project Flow Diagram

```
HTML Files (Wordle pages) 
  ↓ [scrap_wordle_words.py, scrap_all_words.py]
wordle_words.json, all_words.json, black_words.json, red_words.json, green_words.json
  ↓ [words_filter.py]
words_list.json
  ↓ [most_repeating_letters.py] (parallel process)
letters.json
  ↓ [computing_word_score.py]
words_scores.json
  ↓ [wordle_finder.py, score-calculator.py]
Console output (optimal combinations)
```

## Methodology

### 1. Data Collection

The project begins by collecting Wordle words from HTML sources:
- `scrap_all_wordle.py`: Scrapes all possible 5-letter Wordle words
- `scrap_words.py`: Collects words and categorizes them (black/red/green corresponding to Wordle's color system)

### 2. Data Filtering

`words_filter.py` filters words to only include those with unique letters (no letter repetition). This ensures each guess provides information about 5 different letters, maximizing efficiency.

### 3. Letter Position Analysis

`most_repeating_letters.py` analyzes the frequency of each letter at each position (1-5) in Wordle words:
- Creates a dictionary where each letter is associated with its frequency at each position
- This captures how common letters are in specific positions (e.g., 'S' is common at the end but rare at the beginning)
- The results are saved to `letters.json`

### 4. Word Scoring System

`computing_word_score.py` implements a scoring system that assigns points to words based on:
- The frequency of their letters in their respective positions
- Words containing frequently occurring letters in their common positions score higher
- For example, a word with 'E' in position 2 would score higher if 'E' commonly appears second in Wordle words

The formula is:
```
word_score = sum(letter_frequency_at_position for each letter and position)
```

This scoring system prioritizes words that are likely to yield positive results (greens) in Wordle.

### 5. Finding Optimal Combinations

`wordle_finder.py` implements the core algorithm:
- Uses a Trie data structure for efficient word storage and retrieval
- Implements a backtracking algorithm to find valid combinations
- Employs multiprocessing to speed up computation across multiple CPU cores
- Finds combinations of 4 words where no letter is repeated across the combination
- Ranks combinations by their total score

### 6. Score Calculation

`score-calculator.py` provides a utility to calculate scores for specific word combinations for testing and validation.

## Results

The analysis revealed that `['HOWFS', 'IXTLE', 'JUMBY', 'KRANG']` with a score of 2659 is the optimal combination of four words. This combination covers 20 unique letters positioned in ways that maximize information gain according to the letter frequency analysis.

This outperforms the popular combination `['JUNKS', 'WHOMP', 'CALYX', 'FRITZ']` (score: 2464) that has been widely shared online.

## How to Use

1. Run the scripts in sequence:
   - Data collection scripts
   - `words_filter.py`
   - `most_repeating_letters.py`
   - `computing_word_score.py`
   - `wordle_finder.py`

2. Alternatively, use `score-calculator.py` to evaluate specific word combinations:
   ```python
   combination = ["HOWFS", "IXTLE", "JUMBY", "KRANG"]
   ```

## Technical Details

- Implements parallel processing to handle combinatorial complexity
- Uses a Trie data structure to optimize word storage and combination generation
- Employs backtracking algorithm to efficiently search the solution space

## Future Improvements

- Analyze game outcomes using these word combinations
- Include additional constraints based on letter distribution in English
- Develop a web interface for interactive use

## Conclusion

This project demonstrates how data analysis and algorithmic approaches can be applied to optimize game strategy. The identified word combination provides a mathematically sound approach to Wordle that maximizes information gain through strategic initial guesses.
