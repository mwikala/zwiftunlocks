# Zwift Code Entry Automation

This script automates the process of entering secret unlock codes in Zwift by simulating keyboard inputs. It reads codes from a text file (`codes.txt`), opens the code entry window in Zwift, types each code, and submits it.

## Features

- Reads unlock codes from a text file, where each line contains one code.
- Simulates the keyboard presses required to enter the codes in Zwift.
- Includes timing adjustments to ensure smooth operation.

---

## Requirements

- Python 3.6 or higher
- [`pyautogui`](https://pypi.org/project/PyAutoGUI/)

---

## Setup and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/mwikala/zwiftunlocks.git
cd zwiftunlocks
```

### 2. Install Dependencies

Make sure you have Python 3 installed. Then, install the required library:

```bash
pip install pyautogui
```

### 3. Run the Script

Switch to the Zwift application and make sure it is in focus. Then, run the script:

```bash
python zwift_code_entry.py
```

The script will:
1. Simulate pressing `P` to open the unlock code window.
2. Enter each code from the `codes.txt` file.
3. Press `Enter` to submit the code.
4. Wait briefly before moving to the next code.

---

## Notes

- Ensure Zwift is in focus when running the script, as `pyautogui` sends keyboard inputs to the active window.
- Adjust the delay times in the script if Zwift requires more time to process inputs.
- If the `codes.txt` file is missing or empty, the script will notify you and exit.

---

## Troubleshooting

1. **"Error: The file 'codes.txt' was not found."**
   - Ensure the `codes.txt` file exists in the same directory as the script and contains valid codes.
2. **The script types codes too fast.**
   - Increase the delay times in the `time.sleep()` calls within the script.
3. **Keyboard input doesn't work.**
   - Verify Zwift is the active window before starting the script.

---

## Customisation

- **Log Success/Failure**: Modify the script to log results into a separate file if needed.

---

## Disclaimer

This script is provided for educational purposes. Use it responsibly and ensure compliance with Zwift's terms of service.

---

### License

This project is licensed under the MIT License. See the [`LICENSE`](./LICENSE.md) file for details.

