#Valid User Input exercise
#1. username is no more than 12 characters.
#2. username must not contain spaces.
#3. username must not contain digits.

print("1.Username should not me more than 12 characters.\n2.Username must not contain spaces.\n3.Username must not contain digits.")
Username = input("Enter a Username:")

if len(Username) > 12:
    print("Invalid Username. Enter less than 12 characters.")
elif not Username.find(" ") == -1 :
    print("Username should not contain spaces")
elif Username.isalpha() == False :
    print("Usename should not contain any digits")
else:
    print(f"Welcome {Username}")