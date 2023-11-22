import json
import re

def reformat_title(title):
    # Add spacing around punctuation
    title = re.sub(r'([^\w\s])', r' \1 ', title)

    title_arr = title.split()
    reformatted_title = ""
    for word in title_arr:
        if word.isnumeric():
            reformatted_title += "_num_ "
        else:
            reformatted_title += word + " "
    return reformatted_title + "\n"

def main():
    titles_file = open("titles.txt", "w")

    with open('test.json', 'r') as file:
        for line in file:
            print(line)
            try:
                data = json.loads(line)  # Parse the JSON object in each line
                if 'title' in data:
                    reformatted_title = reformat_title(data['title'])
                    titles_file.write(reformatted_title)
            except json.JSONDecodeError:
                pass  # Skip lines that are not valid JSON

if "__main__" == __name__:
    main()
