import csv
f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()
print("You on 4000-most-common-english-words.csv")
def english_most_common_english_words_csv(file):
    most_vowel_word = ""
    average_word_length = 0
    common_starting_letter = ""
    for vowels in file:
        if vowels in ["a", "e", "i", "o", "u"]:
            most_vowel_word = vowels
        return most_vowel_word