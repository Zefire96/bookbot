from collections import Counter

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text_lower = text.lower()
    char_count = Counter(text_lower)
    filtered_char_count = {char: count for char, count in char_count.items() if char.isalpha()}
    return filtered_char_count

filename = "books/frankenstein.txt"

def generate_report(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            word_count = count_words(text)
            char_count = count_characters(text)
            sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
            print(f"--- Begin report of {filename} ---")
            print(f"{word_count} words found in the document\n")
            for char, count in sorted_char_count:
                print(f"The {char} character was found {count} times")
            print(f"--- End report ---")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
filename = "books/frankenstein.txt"
generate_report(filename)