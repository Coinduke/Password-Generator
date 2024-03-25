from random import *
import pyperclip
import time

password = ""
numbers = ["0","1","2","3","4","5","6","7","8","9"]

lower_case_chars = ["a","b","c","d","e",
        "f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",
        "w","x","y","z"]

upper_case_chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
        "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

special_chars = ["!","@","#","$","%",
        ","<",(",")","*","+","-"]

very_special_chars = ["★","÷","➽","♣","♥","♦","♠","☆","✔","‽","⎋"]

keys = []

numchars = input('do you want numbers?(answer yes or no): ')

numchars = numchars.lower()

if numchars == 'yes':
    keys.extend(numbers)
elif numchars == 'no':
    pass
else:
    print("you seem to have made a typo, please reload the code and try again.")
    time.sleep(10)
    quit()

uppercasechars = input('do you want upper case letters?(answer yes or no): ')

uppercasechars = uppercasechars.lower()

if uppercasechars == 'yes':
    keys.extend(upper_case_chars)
elif uppercasechars == 'no':
    pass
else:
    print("you seem to have made a typo, please reload the code and try again.")
    time.sleep(10)
    quit()
lowercasechars = input('do you want lower case letters?(answer yes or no): ')

lowercasechars = lowercasechars.lower()

if lowercasechars == 'yes':
    keys.extend(lower_case_chars)
elif lowercasechars == 'no':
    pass
else:
    print("you seem to have made a typo, please reload the code and try again.")
    time.sleep(10)
    quit()

specialchars = input('do you want special characters like @ ?(answer yes or no): ')

specialchars = specialchars.lower()

if specialchars == 'yes':
    keys.extend(special_chars)
elif specialchars == 'no':
    pass
else:
    print("you seem to have made a typo, please reload the code and try again.")
    time.sleep(10)
    quit()


veryspecialchars = input('do you want very special characters like ★ ?(answer yes or no): ')

if veryspecialchars == 'yes':
    keys.extend(very_special_chars)
elif veryspecialchars == 'no':
    pass
else:
    print("you seem to have made a typo, please reload the code and try again.")
    time.sleep(10)
    quit()

length = int(input("how long do you want your password to be?: "))

if length > 36:
    print("please enter a number smaller than 35")
    time.sleep(10)
    quit()

elif length < 16:
    print("please enter a number larger than 15.")
    time.sleep(10)
    quit()

else:
    for i in range(length):
        x = choice(keys)
        password = str(password) + str(x)
        
print("")
print(password)
pyperclip.copy(password)
print("Password was copied to clipboard")
end_App = input("\nPress enter to close the application:")