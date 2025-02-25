import sys
from stats import main, character_count, dictionary_sort

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 

book_path = sys.argv[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
main(book_path)
print("--------- Character Count -------")
dictionary_sort(character_count(book_path))
print("============= END ===============")