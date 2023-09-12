def count_letters(str):
    characters = {}
    count = 0
    for i in str:
        i = i.lower()
        if i in characters.keys():
            characters[i] += 1
            continue
        else:
            characters.update({i: count+1})
    print(characters)

def count_words(str):
    words = str.split()
    print(len(words))

def read_book(book):
    with open(book) as f:
        content = f.read()
        print(content)
        count_words(content)
        count_letters(content)


def main():
    read_book("books/frankenstein.txt")

main()