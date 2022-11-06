'''A password authentication system is a system that is used for the identification of a user.
Think of it like a login screen that you see while logging in to your Facebook account.
It asks for your email or a username and then it asks for your password.
If you have entered the correct password then it verifies you as the real user.'''

import getpass
database = {"username1":"password1", "username2":"password2"}
username = input("Enter your username : ")
password = getpass.getpass("Enter the password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again! ")
        break
print("Verified")
