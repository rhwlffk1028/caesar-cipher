# alphabet list (reason for having 52 alphabets is because of the cases where users are encoding ending alphabets, such as 'x', 'y', 'z', etc)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# function that takes user inputs (arguments) to encode/decode the message
def encrypt(user_text, user_direction, user_shift):
    encrypt_text = ""
    # if user input was "decode" then -1 flips the sign of the cipher direction
    if user_direction == "decode":
        user_shift *= -1
    # this for loop tracks each characters in user input message
    for char in user_text:
        # this allows to encode/decode character (if they are alphabet)
        if char in alphabet:  
            position = alphabet.index(char)
            new_position = position + user_shift
            encrypt_text += alphabet[new_position]
        # this 'else' condition tracks characters that are not alphabets, such as blank, symbols, or numbers (it means that this function does not encode/decode non-alphabet characters)
        else:
            encrypt_text += char
    # it prints cipher direction and provide encoded/decoded text to user
    print(f"Here's the {user_direction}d result: {encrypt_text}")

# this imports ascii logo from art.py
from art import logo
cipher_logo = logo

# when cipher starts, logo pops up and assign encrypt_again to be 'True' so that while loop runs
print(logo)
encrypt_again = True

# while loop runs as long as user keeps wanting to run this program
while encrypt_again:
    # user will be prompted to provide cipher direction, message, and shift amount
    direction = input("Type 'encode to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    # this is handy when user types high number as a shift amount because it will still be able to look through the alphabet list
    shift = shift % 26

    # this runs the function that outputs endcoded/decoded text per user inputs
    encrypt(text, direction, shift)

    # user will be prompted whether they want to continue or not
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    # if user selects 'no' then while loop stops as encrypt_again changes to False
    if play_again == "no":
        encrypt_again = False
        print("Thanks for playing!")

 


