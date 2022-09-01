import string
import random
def generate_password(L):
    Numbers = string.digits
    Letters = string.ascii_letters
    Symbols = string.punctuation
    seed = Numbers+Letters+Symbols
    password = random.sample(seed, k=L)
    password = "".join(password)
    counter = 0
    if True in [i.isdigit() for i in password]:
        counter += 1
    if True in [i.islower() for i in password]:
        counter += 1
    if True in [i.isupper() for i in password]:
        counter += 1
    if True in [i in Symbols for i in password]:
        counter += 1
    if counter == 4:
        print(password)
    else:
        generate_password(len(password))

def main():
     while True:
         length = input("Hello, Would you tell us the password length? (Between 8-16) ")
         try:
             length = int(length)
             if length in range(8, 17):
                 password = generate_password(length)
                 break
             else:
                print("Something wrong, check password length is between 8 and 16!")
         except ValueError:
            print("Something wrong, Program accept numbers only!")
main()
