from base64 import b64decode, b64encode
import hashlib
from traceback import print_tb
import random
# Main Class
#authors:  Zach, Tyler, Sean, Jonah

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

        passWithSalt = (passwordBytes + b64encode(salt)).decode("utf-8") # Concatenates passwordBytes with Base64 of the salt
        hashedPassWithSalt = hashlib.sha512(passWithSalt.encode("utf-8")) # Applies SHA-512 to passWithSalt
        result = b64encode(hashedPassWithSalt.hexdigest().encode("utf-8")).decode("utf-8") # Applies Base64 to hashedPassWithSalt

        keyBytes = key.encode("utf-8") # Turns the key into a byte representation
        saltWithKey = (salt + b64encode(keyBytes)).decode("utf-8") # Concatenates salt with base64 encoded key
        encodedSaltKey = b64encode(saltWithKey.encode("utf-8")) # Encrypts the salted salt

        file.write(user + ':$6$' + encodedSaltKey.decode("utf-8") + '$' + result + '\n')
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

def check_password(user, password): #Decode and check data

    passwordBytes = str(password).encode('ascii') # Creates a byte representation of the password

    #Gathering file contents to be read 
    fileRead = open('Project2PW.txt', 'r')
    lines = fileRead.readlines()

    for line in lines:
        if line.startswith(user + ":$6$"):
            value = line.split("$")
            value = value[2]
            value = b64decode(value.encode("utf-8").decode("utf8"))
            salt = value[0:16].decode("utf-8") #decode the extracted salt value
            salt = bytes(salt.encode('ascii')) #turn salt into a byter representation

            passWithSalt = (passwordBytes + b64encode(salt)).decode("utf-8") # Concatenates passwordBytes with Base64 of the salt
            hashedPassWithSalt = hashlib.sha512(passWithSalt.encode("utf-8")) # Applies SHA-512 to passWithSalt
            result = b64encode(hashedPassWithSalt.hexdigest().encode("utf-8")).decode("utf-8") # Applies Base64 to hashedPassWithSalt
            
            keyBytes = key.encode("utf-8") # Turns the key into a byte representation
            saltWithKey = (salt + b64encode(keyBytes)).decode("utf-8") # Concatenates salt with base64 encoded key
            encodedSaltKey = b64encode(saltWithKey.encode("utf-8")) # Encrypts the salted salt

            if line.endswith('$6$' + encodedSaltKey.decode("utf-8") + '$' + result + '\n'):
                return True
            else: 
                return False
    return False


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
                add_user(answers[1], answers[2])

        elif answers[0] == "check-password":
            if count <= 1 or count > 3: #amkes sure their is all the info needed
                print("information given does not match the required.")
                break
            else:
                if check_password(answers[1], answers[2]) :
                    print("Your username and password combination is valid")
                else : 
                    print("Your username and password combination is NOT valid")

                
                
                
                
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

# Task 3: The project allows the application to check a user???s password.

# Task 4: The project allows the application to print the password file.

# Task 5: The application correctly saves and loads the password store to/from a file.

# Task 6: Thoroughly document your code.
