import random
import string
length=int(input("Enter the Length of your Password:"))
while 0<length<=15:
    print("Choose what you want to include")
    while True:
        character_pool=[]
        if input('1. Uppercase letters (y/n):')[0].lower()=='y':
            character_pool += string.ascii_uppercase
        if input('2. Lowercase letters (y/n):')[0].lower()=='y':
            character_pool += string.ascii_lowercase
        if input('3. Numbers (y/n):')[0].lower()=='y':
            character_pool += string.digits
        if input('4. Symbols (y/n):')[0].lower()=='y':
            character_pool += string.punctuation
        if character_pool==[]:
            print('Please Select something')
        else:
            a=''
            print(a.join(random.choices(character_pool,k=length)))
        if input('Wanna Try Again?(y/n):')[0].lower()=='y':
            continue
        else:
            break
    break
