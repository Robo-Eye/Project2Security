from base64 import b64encode
import hashlib
# Main Class
# Zach, Tyler, Sean, Jonah


def add_user(user, password):
    file = open('Project2PW.txt', 'w')
    passwordBytes = password.encode('ascii') # Creates a byte representation of the password
    salt = b"2rqP06Msi0fu" # Creates a byte representation of the salt
    passWithSalt = (passwordBytes + b64encode(salt)).decode("utf-8") # Concatenates passwordBytes with Base64 of the salt
    hashedPassWithSalt = hashlib.sha512(passWithSalt.encode("utf-8")) # Applies SHA-512 to passWithSalt
    result = b64encode(hashedPassWithSalt.hexdigest().encode("utf-8")).decode("utf-8") # Applies Base64 to hashedPassWithSalt
    encodedPasswordSalt = b64encode(passWithSalt.encode("utf-8")) # Used to get encodedPasswordSalt after hashtype in manager
    file.write(user + ':$6$' + encodedPasswordSalt.decode("utf-8") + '$' + result)

def remove_user(user): #Decode and delete data
    pass

def check_password(user, password): #Decode and check data
    pass

def print_file(): #Be able to print the file
    pass

def save_to_file(): 
    pass 

def main():
    add_user("alice", "S3cret!Pazw")

if __name__ == "__main__":
    main()

# Task 1: The project allows the application to add a new user to the password store.

# Task 2: The project allows the application to remove a user from the password store.

# Task 3: The project allows the application to check a user’s password.

# Task 4: The project allows the application to print the password file.

# Task 5: The application correctly saves and loads the password store to/from a file.

# Task 6: Thoroughly document your code.
