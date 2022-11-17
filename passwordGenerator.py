#minLength = 0
#set min length. generated password may exceed this
#while minLength < 8:
#    minLength = int(input("What is your desired password length? "))
#    if minLength < 8:
#        print('Password must be at least 8 characters long')

from codecs import encode
import io
import requests
from random import randint

#get list of words if user does not specify a word or phrase 
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()
good_words = list(filter(lambda word: len(word) > 4, WORDS))

specific_word_affirmation = input("Is there a specific word or phrase you would like to include in your password? y/n: ").lower()
if specific_word_affirmation == 'y':
    myWord = input("Enter your word or phrase here: ")
else:
    myWord = good_words[randint(0, len(good_words))].decode('utf-8')

include_spec_char = input("Would you like to include special characters? y/n: ").lower()
include_num = input("Would you like to include numbers? y/n: ").lower()


def special_characters_array():
    char_codes = []
    i = 33
    while i <= 48:
        char_codes.append(i)
        i+=1
    i = 58
    while i <= 64:
        char_codes.append(i)
        i+=1
    i = 91
    while i <= 96:
        char_codes.append(i)
        i+=1
    return char_codes
