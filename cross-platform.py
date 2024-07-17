import os
import getpass

def get_username():
    try:
        username = os.getlogin()
        # Alternatively, you can use getpass.getuser()
        # username = getpass.getuser()
        return username
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
username = get_username()
if username:
    print(f"The current username is: {username}")
else:
    print("Failed to determine the username.")
