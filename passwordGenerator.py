import requests
from random import randint

def random_word(capitilize = False):
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    good_words = list(filter(lambda word: len(word) > 4, WORDS))
    response = good_words[randint(0, len(good_words))].decode('utf-8')
    if capitilize:
        response = response.capitalize()
    return response

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
    char_codes = list(map(lambda char: chr(char), char_codes))
    return char_codes

specific_word_affirmation = input("Is there a specific word or phrase you would like to include in your password? y/n: ").lower()
if specific_word_affirmation == 'y':
    my_word = input("Enter your word or phrase here: ")
else:
    my_word = random_word()

include_capitals = input("Does your password require both uppercase and lowercase letters? y/n: ").lower()
include_capitals = True if include_capitals == 'y' else False

include_spec_char = input("Would you like to include special characters? y/n: ").lower()
include_spec_char = True if include_spec_char == 'y' else False

include_num = input("Would you like to include numbers? y/n: ").lower()
include_num = True if include_num == 'y' else False

min_length = 0
while min_length <= 6 or min_length > 30:
    desired_length = input("What is the minimum length for your password?: ")
    try: 
        int(desired_length)
    except:
        desired_length = 0
    if int(desired_length) <= 6 or int(desired_length) > 100:
        print("Miminum length must be an integer of at least 6 and less than 100")
    min_length = int(desired_length)

password = my_word
print(password)
if not include_spec_char and not include_num:
    while len(password) < min_length:
        # print('adding letters', password)
        password = password + random_word(include_capitals)

print(password) 