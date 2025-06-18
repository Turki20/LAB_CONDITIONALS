

name:str = input("Enter your name: ")
email:str = input("Enter your email: ")


if len(name) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name.")
else:    
    if email.find("@gmail") > 0 and len(email) > (len("@gmail") + 2):
        print(f"welcome {name}, you registered with the email {email} !")
    else:
        print("the email is not valid , please provide a valid email .")