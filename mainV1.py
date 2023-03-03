import hashlib

PASSWORD_LENGTH = 12

# Function to hash a string using BLAKE2
def hash_string(string):
    return hashlib.blake2b(string.encode(), digest_size=(int(PASSWORD_LENGTH/2))).hexdigest()

# Main function
def main():
    # Get the website and password from the user
    website = input("Enter site: ")
    password = input("Enter password: ")

    # Combine the username and password and hash the result
    combined_string = website + password
    hashed_password = hash_string(combined_string)

    # Print the hashed password
    print("\nHashed password:", hashed_password)

if __name__ == "__main__":
    main()
