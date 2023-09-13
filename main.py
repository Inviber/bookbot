def count_letters(str):
    characters = {}
    count = 0
    for i in str:
        i = i.lower()
        if i in characters.keys():
            characters[i] += 1
            continue
        else:
            if i.isalpha():
                characters.update({i: count+1})
    return characters

def count_words(str):
    words = str.split()
    return len(words)

def book_report(book, words, characters):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words in the document\n")
    report = dict(reversed(sorted(characters.items(), key=lambda item: item[1])))
    for i in report:
        print(f"The '{i}' was found {report[i]} times")
    print("--- End Report ---")

def read_book(book):
    with open(book) as f:
        content = f.read()
        print(content)
        print(count_words(content))
        print(count_letters(content))
        book_report(book, count_words(content), count_letters(content))

def main():
    read_book("books/frankenstein.txt")

main()