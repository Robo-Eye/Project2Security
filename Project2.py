import base64
import hashlib
# Main Class
# Zach, Tyler, Sean, Jonah

def add_user(username, password): #This is where we will encode
    salt = '2rqP06Msi0fu'
    return(print(base64.encode(hashlib.sha512(password + base64.encode(salt))))) #add to file later

def remove_user(username): #Decode and delete data
    pass

def check_password(username, password): #Decode and check data
    pass

def print_file(): #Be able to print the file
    pass

def save_to_file(): 
    pass 

def main():
    pass

if __name__ == "__main__":
    main()

# Task 1: The project allows the application to add a new user to the password store.

# Task 2: The project allows the application to remove a user from the password store.

# Task 3: The project allows the application to check a user’s password.

# Task 4: The project allows the application to print the password file.

# Task 5: The application correctly saves and loads the password store to/from a file.

# Task 6: Thoroughly document your code.
