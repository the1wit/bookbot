from stats import get_num_words, get_num_characters, sort_data
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # url = "books/frankenstein.txt"
    url = sys.argv[1]
    text = get_book_text(url)
    num_words = get_num_words(text)

    num_characters = get_num_characters(text)
    sorted_data = sort_data(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {url}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for field in sorted_data:
        print(f"{field["char"]}: {field["num"]}")


main()
