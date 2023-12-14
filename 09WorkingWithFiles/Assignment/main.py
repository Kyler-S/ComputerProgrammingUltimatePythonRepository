import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()


print("You on 4000-most-common-english-words.csv")
def word_with_most_vowels(wordlist):
    most_vowel_word = ""
    for vowels in wordlist:
        if vowels == "a":
            most_vowel_word = vowels
        return most_vowel_word
    
print(word_with_most_vowels(words))