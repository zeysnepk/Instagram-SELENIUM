def get_credentials():
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    
    username = str(username_input)
    password = str(password_input)
    
    # Save credentials to info.txt file for future use
    with open("info.txt", "w") as file:
        file.write(f"{username}\n{password}")
    
    return username, password

def read_info():
    # Read saved credentials from info.txt file
    try:
        with open("info.txt", "r") as file:
            username = file.readline().strip()
            password = file.readline().strip()
            return username, password
    except FileNotFoundError:
        print("Credentials file not found. Please run info.py first.")
        exit()
    
# Call this script from the terminal to get and save your login credentials
if __name__ == "__main__": 
    username, password = get_credentials()
    print(f"Username: {username}, Password: {password}")
