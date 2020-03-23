"""Create a JSON dictionary of keyword -> shortest synonym."""
import requests

URL = "https://raw.githubusercontent.com/words/moby/master/words.txt"


def main():
    response = requests.get(URL)
    text = response.text

    thesaurus = {}

    lines = text.split("\n")
    for line in lines:
        words = line.split(",")
        keyword = words[0]
        shortest_synonym = keyword
        for word in words[1:]:
            if len(shortest_synonym) > len(word):
                shortest_synonym = word
        if shortest_synonym != keyword:
            thesaurus[keyword] = shortest_synonym


main()
