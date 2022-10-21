from base64 import b64encode
import hashlib
# Main Class
# Zach, Tyler, Sean, Jonah

def add_user(user, password): #This is where we will encode
    file = open('Project2PW.txt', 'w')
    passwordBytes = password.encode('ascii')
    salt = b"2rqP06Msi0fu"
    file.write((passwordBytes + b64encode(salt)).decode("utf-8")) #inner part

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
