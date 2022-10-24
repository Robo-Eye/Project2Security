from base64 import b64decode, b64encode
import hashlib
from traceback import print_tb
import random
# Main Class
# Zach, Tyler, Sean, Jonah

key = "aeiouqwertyabc3120" # Normally this would be stored in a separate server, would be secret

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
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        chars=[]
        for i in range(16):
            chars.append(random.choice(ALPHABET))
        salt = "".join(chars).encode('ascii') # Creates a randomly generated salt
        
        saltFile = open('salts.txt', 'a') # Either creates or appends to a salt file that can only be read with key
        keyBytes = key.encode("utf-8") # Turns the key into a byte representation
        saltWithKey = (salt + b64encode(keyBytes)).decode("utf-8") # Concatenates salt with base64 encoded key
        encodedSaltKey = b64encode(saltWithKey.encode("utf-8")) # Encrypts the salted salt
        saltFile.write(user + ':' + encodedSaltKey.decode("utf-8") + '\n') # Writes the salted salt to the salt file

        passWithSalt = (passwordBytes + b64encode(salt)).decode("utf-8") # Concatenates passwordBytes with Base64 of the salt
        hashedPassWithSalt = hashlib.sha512(passWithSalt.encode("utf-8")) # Applies SHA-512 to passWithSalt
        result = b64encode(hashedPassWithSalt.hexdigest().encode("utf-8")).decode("utf-8") # Applies Base64 to hashedPassWithSalt
        encodedPasswordSalt = b64encode(passWithSalt.encode("utf-8")) # Used to get encodedPasswordSalt after hashtype in manager
        file.write(user + ':$6$' + encodedPasswordSalt.decode("utf-8") + '$' + result + '\n')
        print("User: " + user + " has succesfully been added to system.")
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
                print("User: " + user + " has succesfully been removed from the system.")
    if removed == False:
        print("We could not find '" + user + "' in our system, please try again")
    else: #remove from salt file as well
        saltFileRead = open('salts.txt', 'r') # Opens the salt file for reading
        saltLines = saltFileRead.readlines() # Gathers lines to read in salt file
        with open("salts.txt", "w") as saltFile:
            for line in saltLines:
                if not line.startswith(user + ":"):
                    saltFile.write(line) # Rewrites the lines that aren't the user specified

def check_password(user, password): #Decode and check data

    passwordBytes = password.encode('ascii') # Creates a byte representation of the password

    #Gathering file contents to be read 
    fileRead = open('Project2PW.txt', 'r')
    lines = fileRead.readlines()
    saltRead = open('salts.txt', 'r')
    saltLines = saltRead.readlines()

    for saltLine in saltLines:
        if saltLine.startswith(user + ":"):
            value = saltLine.split()[-1]
            value = b64decode(value.encode("utf-8"))
            salt = value[:-16]

            #encoding the user input the same way as the stored password 
            passWithSalt = (passwordBytes + b64encode(salt)).decode("utf-8") # Concatenates passwordBytes with Base64 of the salt
            hashedPassWithSalt = hashlib.sha512(passWithSalt.encode("utf-8")) # Applies SHA-512 to passWithSalt
            result = b64encode(hashedPassWithSalt.hexdigest().encode("utf-8")).decode("utf-8") # Applies Base64 to hashedPassWithSalt
            encodedPasswordSalt = b64encode(passWithSalt.encode("utf-8")) # Used to get encodedPasswordSalt after hashtype in manager

            for line in lines:
                if line.startswith(user + ":"):
                    if line.endswith(encodedPasswordSalt):
                        return True
                    else: 
                        return False
    
    return False 

    

    #Hashing password to compare with sotred password
    passwordBytes = password.encode('ascii') # Creates a byte representation of the password
    salt = b"2rqP06Msi0fu" # Creates a byte representation of the salt (Perhaps randomly generate)
    passWithSalt = (passwordBytes + b64encode(salt)).decode("utf-8") # Concatenates passwordBytes with Base64 of the salt
    hashedPassWithSalt = hashlib.sha512(passWithSalt.encode("utf-8")) # Applies SHA-512 to passWithSalt
    result = b64encode(hashedPassWithSalt.hexdigest().encode("utf-8")).decode("utf-8") # Applies Base64 to hashedPassWithSalt
    encodedPasswordSalt = b64encode(passWithSalt.encode("utf-8")) # Used to get encodedPasswordSalt after hashtype in manager

    #Comparing the user input with the hashed password 
    with open("Project2PW.txt", "r"):
        for line in lines: 
            if line.startswith(user + ":"):
                if line.endswith(encodedPasswordSalt):
                    return True
                else:
                    return False
            else:
                print("No such user in directory.")
    
                


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
        count = len(answers)
        if answers[0] == "add-user":
            if count <= 1 or count > 3: #amkes sure their is all the info needed
                print("information given does not match the required")
                break
            else: #if the user enter the valid amount of info the add_user function will be reached
                print(answers)
                add_user(answers[1], answers[2])

        elif answers[0] == "check-password":
            if count <= 1 or count > 3: #amkes sure their is all the info needed
                print("information given does not match the required.")
                break
            else:
                check_password(answers[1], answers[2])
        elif answers[0] == "remove-user":
            if count <= 1 or count > 2: #amkes sure their is all the info needed
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
