"""Create a JSON dictionary of keyword -> shortest synonym."""
import requests

URL = "https://raw.githubusercontent.com/words/moby/master/words.txt"
OUTPUT_FILE = "thesaurus.csv"

def main():
    response = requests.get(URL)
    text = response.text

    thesaurus = {}
    out_file = open(OUTPUT_FILE, 'w')

    lines = text.split("\n")
    for line in lines:
        words = line.split(",")
        keyword = words[0]
        shortest_synonym = keyword
        for word in words[1:]:
            if len(shortest_synonym) > len(word) > 2:
                shortest_synonym = word
        if shortest_synonym != keyword:
            thesaurus[keyword] = shortest_synonym
            print(keyword, "->", shortest_synonym)
            print("{},{}".format(keyword, shortest_synonym, file=out_file)

    out_file.close()


main()
