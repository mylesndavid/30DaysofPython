from cryptography.fernet import Fernet

def fetchKey():
    with open("thekey.key","rb") as key:
        secret = key.read()
        return secret


def decrypt(text):
    with open("thekey.key", "rb") as key:
        decryptedText = Fernet(key.read()).decrypt(text.encode())
        return decryptedText.decode()


def list():
    print("Stored Accounts")
    with open("passwords.txt","r") as f: 
        for line in f.readlines():
            data = line.rstrip()
            account,user,passw = data.split("|")
            print(account)
        actname = input("Type name of account you wish to access")
    with open("passwords.txt","r") as f:
        for line in f.readlines():
                if actname in line:
                    data = line.rstrip()
                    account,user,passw = data.split("|")
                    print(f"Account name:\n{account}\nCredentials:\n{user}|{passw}")
                    sel = input("Type 'v' to view password in plain text")
                    if sel == "v":
                        print(decrypt(passw))




def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            account,user,passw = data.split("|")
            print("Account Name: ",account,"User: ",user,"Password: ",passw)

def add(secret):
    acct = input('Account Name: ')
    usr = input('Username: ')
    pwd = input('Password: ')

    epwd = Fernet(secret).encrypt(pwd.encode())
    with open('passwords.txt', 'a') as f:
        f.write(acct + "|" + usr + "|" + epwd.decode() + "\n")

