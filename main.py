from stats import count_words
from stats import count_characters
from stats import sort_dict
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    #this_book = "books/frankenstein.txt"
    this_book = sys.argv[1]
    book_text = get_book_text(this_book)
    num_words = count_words(book_text)
    #print(f"Found {num_words} total words")
    num_characters = count_characters(book_text)
    #print(num_characters)
    sorted_characters = sort_dict(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {this_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char,count in sorted_characters.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")





main()
    