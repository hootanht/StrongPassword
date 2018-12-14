import string
import random


def CreatePassWord(passwordLength):
    password = string.ascii_letters + string.digits + "!@#$%^&*()_+?><|"
    passwordList = []
    for charpass in range(passLength):
        passchar = random.choice(password)
        passwordList.append(passchar)
    finalpassword = "".join(passwordList)
    return finalpassword


while True:
    passLength = int(input("Please Type Your Password Lenght : "))
    print(CreatePassWord(passLength))
    reply = input("Do You Want To Create Another Password ? (Y,N)")
    if reply.lower() == "y":
        pass
    if reply.lower() == "n":
        break
