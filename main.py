def count_words(str):
    words = str.split()
    print(len(words))

def read_book(book):
    with open(book) as f:
        content = f.read()
        print(content)
        count_words(content)

def main():
    read_book("books/frankenstein.txt")

main()