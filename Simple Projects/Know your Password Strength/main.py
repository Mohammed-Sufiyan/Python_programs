import string
import getpass

def check_password_strength(password):
    lower_alpha_count = upper_alpha_count = number_count = whitespace_count = special_char_count = 0
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        elif char == " ":
            whitespace_count += 1
        else:
            special_char_count += 1
    strength = 0
    remarks = ""
    if lower_alpha_count >= 1:
        strength += 1
    if upper_alpha_count >= 1:
        strength += 1
    if number_count >= 1:
        strength += 1
    if whitespace_count >= 1:
        strength += 1
    if special_char_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "That's a very bad password. Change it as soon as possible."
    if strength == 2:
        remarks = "That's not a good password. You should consider making a tougher password."
    if strength == 3:
        remarks = "Your password is okay, but it can be improved a lot."
    if strength == 4:
        remarks = "Your password is hard to guess, But you can make it even more secure."
    if strength == 5:
        remarks = "Now that's one hell of a strong password!!! Hackers don't have a chance guessing that passsword."

    print("Your password has :- ")
    print(f"{lower_alpha_count} lowercase letters")
    print(f"{upper_alpha_count} uppercase letters")
    print(f"{number_count} digits")
    print(f"{special_char_count} special characters")
    print(f"{whitespace_count} whitespaces")
    print(f"Remarks : {remarks}")

print("==== Welcome to Password Strength Checker ====")
while 1:
    choice = input("Do you want to check a password's strength 1 for yes & 0 for no :- ")
    if "1" in choice.lower():
        password = getpass.getpass("Enter the password : ")
        check_password_strength(password)
    elif "0" in choice.lower():
        print("Exiting....")
        break
    else:
        print("Invalid input... Please try again.")
    print()
