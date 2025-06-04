import sys
from stats import get_num_words, get_num_characters, sorted_list_of_characters

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    #print(f"{get_num_words(book_text)} words found in the document")
    #print(get_num_characters(book_text))
    sorted_list_of_characters(get_num_characters(book_text), get_num_words(book_text), sys.argv[1])

main()