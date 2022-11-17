#minLength = 0
#set min length. generated password may exceed this
#while minLength < 8:
#    minLength = int(input("What is your desired password length? "))
#    if minLength < 8:
#        print('Password must be at least 8 characters long')

import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()
goodwords = list(filter(lambda word: len(word) > 4, WORDS))
print([1000].decode('utf-8'))

specificWordAffirmation = input("Is there a specific word or phrase you would like to include in your password? y/n: ").lower()
if specificWordAffirmation == 'y':
    myWord = input("Enter your word or phrase here: ")
else:
    print('ok ')


includeSpecChar = input("Would you like to include special characters? y/n: ").lower()
includeNum = input("Would you like to include numbers? y/n: ").lower()
