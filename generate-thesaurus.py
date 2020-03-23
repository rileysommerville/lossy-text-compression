"""Create a JSON dictionary of keyword -> shortest synonym."""
import requests

URL = "https://raw.githubusercontent.com/words/moby/master/words.txt"


def main():
    response = requests.get(URL)
    text = response.text


main()
