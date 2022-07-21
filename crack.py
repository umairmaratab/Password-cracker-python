import hashlib
from hmac import digest

pass_hash = input("Enter md5 hash:  ")

wordlist = input("File name: ")

try:
    pass_file = open(wordlist,"r")
except:
    print("No file found")
    quit()

for word in pass_file:
    # In python when u trying to hash a string it should in UTF-8
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest() # creating hash

    print(word)
    print(digest)
    print(pass_hash)
    # if password found
    if digest == pass_hash:
        print("Password found")
        print("password is : " + word)
        flag = 1
        break

if flag == 0:
    print("password/pharase not in the list")
