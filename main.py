import sys

from stats import count_words, count_characters, sort_characters_count

def get_book_text(fp):
    with open(fp) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    fp = sys.argv[1]
    booktext = get_book_text(fp)
    num_words = count_words(booktext)

    char_count = sort_characters_count(count_characters(booktext))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fp}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in char_count:
        print(f"{i['character']}: {i['count']}")
    print("============= END ===============")

main()