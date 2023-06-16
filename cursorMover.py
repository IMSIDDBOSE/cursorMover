# This is just a fun tiny Program to just Move the mouse cursor of your system.

import pyautogui
import time
import random

while True:
    try:
        # Generate random offsets for x and y coordinates
        x_offset = random.randint(-10, 10)
        y_offset = random.randint(-10, 10)
        
        # Get current cursor position
        current_x, current_y = pyautogui.position()
        
        # Calculate new coordinates by adding the offsets
        new_x = current_x + x_offset
        new_y = current_y + y_offset
        
        # Move the mouse cursor to the new position
        pyautogui.moveTo(new_x, new_y, duration=0.1)
        
        # Wait for 1 second before the next movement
        time.sleep(1)
    
    except KeyboardInterrupt:
        # Exit the loop if Ctrl+C is pressed
        break
