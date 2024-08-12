import random
import string

special_char = string.punctuation
letters = string.ascii_letters
numbers = string.digits
print("-------------------------------------\n"
      "----Welcome to Password Generator----\n"
      "-------------------------------------")
user_input = int(input('Enter The Length of The Password : '))

all_char = [
    random.choice(letters),
    random.choice(numbers),
    random.choice(special_char)
]
password = ['']
password += [random.choice(all_char) for i in range(0, user_input)]
gen_password = ''.join(password)
print('Your Password is :' + gen_password)
