from cryptography.fernet import Fernet
from modes import *



master_pwd = input("What is the master password?")

if master_pwd == "urmom":

    while True:
        mode = input('Would you like to add a new password or view existing ones (view,add,list)? /n You can also generate a new private key by typing "Key"\n')
        match mode:
            case "view":
                view()
            case "add":
                add(fetchKey())
            case "list":
                list()
            case "q":
                break
            case "key":
                key = Fernet.generate_key()
                with open("thekey.key", "wb") as thekey:
                        thekey.write(key)
                print("New key generated")
            case other: # can also be written case _
                print("this is not a valid selection")
                continue
else: print("Wrong password")