import pyautogui
import pygetwindow as gw
import time
from PIL import Image


def capture_bluestacks_screenshot():
    interval = 0.5

    count = 0
    while True:
        # Get the Bluestacks window
        bluestacks_window = None
        for window in gw.getAllTitles():
            if 'BlueStacks App Player' in window:  # Find the window with Bluestacks in the title
                bluestacks_window = gw.getWindowsWithTitle(window)[0]
                break

        if bluestacks_window:
            # Get window's dimensions (position and size)
            left, top, width, height = bluestacks_window.left, bluestacks_window.top, bluestacks_window.width, bluestacks_window.height

            # Take screenshot of the Bluestacks window area
            screenshot = pyautogui.screenshot(region=(left, top, width, height))

            # Save the screenshot
            screenshot.save(f"data/state_{count}.png")
            print(f"data/state_{count} saved.")

            count += 1

        else:
            print("Bluestacks window not found!")

        # Wait 1 second before taking the next screenshot
        time.sleep(interval)


if __name__ == "__main__":
    capture_bluestacks_screenshot()
