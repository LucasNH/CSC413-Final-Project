import json
from collections import Counter
import re

# Function to extract unique words from a given text
def extract_unique_words(text):
    # Use regex to split the text into words
    words = re.findall(r'\w+', text.lower())  # Convert to lowercase and split into words
    return set(words)

def main():
    # Initialize a Counter to count unique words
    unique_word_counter = Counter()

    # Open the JSON file and process it line by line
    # File from https://www.kaggle.com/datasets/Cornell-University/arxiv/
    with open('arxiv-metadata-oai-snapshot.json', 'r') as file:
        for line in file:
            try:
                data = json.loads(line)  # Parse the JSON object in each line
                if 'title' in data:
                    title = data['title']
                    unique_words = extract_unique_words(title)
                    unique_word_counter.update(unique_words)
            except json.JSONDecodeError:
                pass  # Skip lines that are not valid JSON

    # Count the total number of unique words
    total_unique_words = len(unique_word_counter)

    # Print the result
    print(f"Total number of unique words in 'title': {total_unique_words}")

if "__main__" == __name__:
    main()
