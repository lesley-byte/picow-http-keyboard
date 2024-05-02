# Write your code here :-)
import time
import random
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Set up HID
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)


def type_like_human(text, base_delay=0.1, typo_rate=0.05):
    """Types out text with variable delays and simulates typos and corrections."""
    i = 0
    while i < len(text):
        char = text[i]
        delay = base_delay + random.uniform(-0.05, 0.1)

        # Introduce natural pauses at punctuation and spaces
        if char in '.!?':
            delay += 0.4
        if char == ' ':
            delay += 0.15

        # Randomly introduce typos based on the typo_rate
        if random.random() < typo_rate:
            # Type a wrong character (typo)
            wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
            layout.write(wrong_char)
            time.sleep(delay)

            # Backspace the wrong character
            layout.write('\x08')  # ASCII character for backspace
            time.sleep(base_delay)

            # Type the correct character
            layout.write(char)
            time.sleep(delay)
        else:
            layout.write(char)
            time.sleep(delay)
        i += 1
