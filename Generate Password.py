import string
import random

s1 = list(string.ascii_lowercase)              # Getting List Of Lower alphabet Characters
s2 = list(string.ascii_uppercase)              # Getting List Of Lower alphabet Characters
s3 = list(string.punctuation)                  # Getting List Of Lower alphabet Characters
s4 = list(string.digits)                       # Getting List Of Lower alphabet Characters
random.shuffle(s1)                             # Shuffle The List
random.shuffle(s2)                             # Shuffle The List
random.shuffle(s3)                             # Shuffle The List
random.shuffle(s4)                             # Shuffle The List

flag = 0                                       # Flag To Get out Of While Once I Get The Accurate Number
password = []                                  # To Store The Generated Password

while flag == 0:
    Character_Count = input("Please Enter How MAny Characters Do You Want [ At Least 6 ] = ")
    try:
        if int(Character_Count) < 6:
            print("You need At Least 6 Characters!")
        else:
            flag = 1
    except:
        print("You Need To Enter Only Numbers !")

part1 = round(int(Character_Count) * (30 / 100))        # Getting 30% of User Input Count
part2 = round(int(Character_Count) * (20 / 100))        # Getting 20% of User Input Count

for i in range(part1):                                  # Fill in Password List By Alphabet Chars
    password.append(s1[i])
    password.append(s2[i])
for i in range(part2):                                  # Fill in Password List By Digits And Punctuations
    password.append(s3[i])
    password.append(s4[i])
password = "".join(password[0:])                        # Converting The List Elements To be One Word
print(password)                                         # Print Out The Generated Password
