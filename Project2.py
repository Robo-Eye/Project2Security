from base64 import b64encode
import hashlib
from traceback import print_tb
# Main Class
# Zach, Tyler, Sean, Jonah


def add_user(user, password):
    fileRead = open('Project2PW.txt', 'r')
    Lines = fileRead.readlines()
    skip = False # Determines whether to skip adding user
    for line in Lines: # Sets up for loop to check if user is already in the file
        if line.startswith(user + ":"):
            skip = True
    if skip == False:
        file = open('Project2PW.txt', 'a')
        passwordBytes = password.encode('ascii') # Creates a byte representation of the password
        salt = b"2rqP06Msi0fu" # Creates a byte representation of the salt (Perhaps randomly generate)
        passWithSalt = (passwordBytes + b64encode(salt)).decode("utf-8") # Concatenates passwordBytes with Base64 of the salt
        hashedPassWithSalt = hashlib.sha512(passWithSalt.encode("utf-8")) # Applies SHA-512 to passWithSalt
        result = b64encode(hashedPassWithSalt.hexdigest().encode("utf-8")).decode("utf-8") # Applies Base64 to hashedPassWithSalt
        encodedPasswordSalt = b64encode(passWithSalt.encode("utf-8")) # Used to get encodedPasswordSalt after hashtype in manager
        file.write(user + ':$6$' + encodedPasswordSalt.decode("utf-8") + '$' + result + '\n')
    else:
        print("User " + user + " is already in our system, please use a different username")

def remove_user(user):
    fileRead = open('Project2PW.txt', 'r') # Opens the file for reading
    Lines = fileRead.readlines() # Gathers lines to read in file
    removed = False # Checks to see if user could be found and removed
    with open("Project2PW.txt", "w") as file:
        for line in Lines:
            if not line.startswith(user + ":"):
                file.write(line) # Rewrites the lines that aren't the user specified
            else:
                removed = True # Line with specified user is not rewritten, removed is now true
    if removed == False:
        print("We could not find '" + user + "' in our system, please try again")

def check_password(user, password): #Decode and check data
    pass

def print_file(): #Be able to print the file
    #try catch block to see if the file exists, if not it will print the error message.
    try:
        fileRead = open('Project2PW.txt', 'r') # Opens the file for reading
        print(fileRead.read())
    except:
        print("No such file can be found in the directory.")

def save_to_file(): 
    pass 

def main():
    answer = ""
    while answer != "end":
        #general information prompted to the user
        print("Welcome to the Secure Password Storage for Password Authentication Project!")
        print("Developers: Tyler F.  Jonah D.  Sean M.  Zack O.")
        print("Possible Commands:\n> add-user [USERNAME] [PASSWORD]\n> check-password [USERNAME] [PASSWORD]\n> remove-user [USERNAME]\n> print\n> end")
        answer = input("Enter Command: ") #gathers user's input
        #switch logic
        answers = answer.split(" ") #splits the one line answer into multiple parts to easily parse info into functions
        if answers[0] == "add-user":
            if answers.count() <= 1 or answers.count() > 3: #amkes sure their is all the info needed
                print("information given does not match the required")
                break
            else: #if the user enter the valid amount of info the add_user function will be reached
                add_user(answer[1], answer[2])

        elif answers[0] == "check-password":
            if answers.count() <= 1 or answers.count() > 3: #amkes sure their is all the info needed
                print("information given does not match the required.")
                break
            else:
                #check_password()
                print("check password method here")
        elif answers[0] == "remove-user":
            if answers.count() <= 1 or answers.count() > 2: #amkes sure their is all the info needed
                print("information given does not match the required")
                break
            else: 
                remove_user(answers[1])
        elif answer == "print":
            print_file()
        elif answer == "end":
            print("program terminated.")
        else:
            print("Invalid command please try again.")
    pass

if __name__ == "__main__":
    main()

# Task 1: The project allows the application to add a new user to the password store.

# Task 2: The project allows the application to remove a user from the password store.

# Task 3: The project allows the application to check a user’s password.

# Task 4: The project allows the application to print the password file.

# Task 5: The application correctly saves and loads the password store to/from a file.

# Task 6: Thoroughly document your code.
