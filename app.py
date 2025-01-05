import pyautogui
import time

# File containing the unlock codes, one per line
codes_file = "codes.txt"

# Read the codes from the text file
def load_codes(file_path):
    try:
        with open(file_path, "r") as file:
            codes = [line.strip() for line in file if line.strip()]
        return codes
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

# Delay to allow user to switch to the Zwift window
print("Switch to Zwift. The script will start in 5 seconds...")
time.sleep(5)

# Function to enter codes
def enter_codes(code_list):
    for code in code_list:
        print(f"Entering code: {code}")
        pyautogui.press("p")          # Press 'P' to open the code entry window
        time.sleep(1)                 # Short delay for the window to open
        pyautogui.typewrite(code)     # Type the code
        time.sleep(0.5)               # Short delay for typing
        pyautogui.press("enter")      # Press 'Enter' to submit the code
        time.sleep(2)                 # Delay to ensure the code is processed

# Load the codes from the file
codes = load_codes(codes_file)

# Execute the function if codes are available
if codes:
    enter_codes(codes)
    print("All codes have been entered!")
else:
    print("No codes to process. Ensure the 'codes.txt' file is properly formatted.")
