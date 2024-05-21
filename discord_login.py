import os
import time
import requests
import getpass
from tqdm import tqdm
import pyperclip
import sys

def clear_screen():
    # Clear screen for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art():
    ascii_art = r"""
  _____               _    _   _ _       _       ____   ___  
 / ____|             | |  | \ | (_)     (_)     |___ \ / _ \ 
| |  __ _ __ ___  ___| | _|  \| |_ _ __  _  __ _  __) | | | |
| | |_ | '__/ _ \/ _ \ |/ / . ` | | '_ \| |/ _` ||__ <| | | |
| |__| | | |  __/  __/   <| |\  | | | | | | (_| |___) | |_| |
 \_____|_|  \___|\___|_|\_\_| \_|_|_| |_| |\__,_|____/ \___/ 
                                        _/ |                  
                                       |__/                   
"""
    print(ascii_art)

def login_to_discord():
    clear_screen()
    print("Discord Login")
    email = input("Email: ")
    password = getpass.getpass(prompt='Password: ')

    # URL for Discord API login endpoint
    login_url = 'https://discord.com/api/v9/auth/login'

    # Payload with login credentials
    payload = {
        'login': email,
        'password': password
    }

    # Print ASCII art
    print_ascii_art()

    # Simulating a loading delay for demonstration purposes
    for _ in tqdm(range(10), desc="Starting", unit=""):
        time.sleep(0.1)

    # Perform the login request
    with tqdm(desc="Logging in", unit="") as pbar:
        response = requests.post(login_url, json=payload)
        pbar.update(1)

    # Check if login was successful
    if response.status_code == 200:
        print("\nLogin successful!")
        # Extract the token from the response
        data = response.json()
        token = data.get('token')
        user_id = data.get('user_id')
        print(f"Token: {token}")
        print(f"User ID: {user_id}")
        # Copy token to clipboard
        pyperclip.copy(token)
        print("Token copied to clipboard!")
        # Wait for 5 seconds before closing
        time.sleep(5)
        sys.exit(0)
    else:
        print("\nLogin failed!")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        # Wait for 5 seconds before closing
        time.sleep(5)
        sys.exit(1)

if __name__ == '__main__':
    login_to_discord()

# Close command prompt window
os.system('exit' if os.name == 'nt' else 'exit()')
