with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def word_count(text):
    words = text.split()
    return len(words)


def letter_count(text):
    lower_text = text.lower()
    letters = {}
    for letter in lower_text:
        if letter in letters and letter.isalpha():
            letters[letter] += 1
        elif letter.isalpha():
            letters[letter] = 1
    return letters


def report(text):
    num_of_words = word_count(text)
    letters_dict = letter_count(text)
    letters_list = []
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document\n")
    for letter in letters_dict:
        letters_list.append(letter)
    letters_list.sort()
    for letter in letters_list:
        print(f"The {letter} character was found {letters_dict[letter]} times")
    print("--- End report ---")


report(file_contents)
