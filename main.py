from stats import count_words

def get_book_text(fp):
    with open(fp) as f:
        return f.read()

def main():
    booktext = get_book_text("books/frankenstein.txt")
    num_words = count_words(booktext)
    print(f"{num_words} words found in the document")

main()