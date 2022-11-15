minLength = 0
#set min length. generated password may exceed this
while minLength < 8:
    minLength = int(input("What is your desired password length? "))
    if minLength < 8:
        print('Password must be at least 8 characters long')
specificWordAffirmation = input("Is there a specific word or phrase you would like to include in your password? y/n").lower()
myWord = ''
if specificWordAffirmation:
    myWord = input("Enter your word or phrase here: ")

includeSpecChar = input("Would you like to include special characters? y/n: ").lower()
includeNum = input("Would you like to include numbers? y/n: ").lower()
