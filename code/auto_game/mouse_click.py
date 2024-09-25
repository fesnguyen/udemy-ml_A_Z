import pygetwindow as gw
import time
import win32api, win32con

def click_at_coordinates(x, y):
    # Simulate mouse click without moving the actual cursor
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def click_bluestacks_center():
    while True:
        # Get the Bluestacks window
        bluestacks_window = None
        for window in gw.getAllTitles():
            if 'BlueStacks App Player' in window:
                bluestacks_window = gw.getWindowsWithTitle(window)[0]
                break

        if bluestacks_window:
            # Get window's dimensions (position and size)
            left, top, width, height = bluestacks_window.left, bluestacks_window.top, bluestacks_window.width, bluestacks_window.height

            # Calculate center of the Bluestacks window
            center_x = left + width // 2
            center_y = top + height // 2

            # Simulate a mouse click at the center of Bluestacks window
            click_at_coordinates(center_x, center_y)

            print(f"Clicked at the center of Bluestacks window at ({center_x}, {center_y})")

        else:
            print("Bluestacks window not found!")

        # Wait for 5 seconds before clicking again
        time.sleep(5)

if __name__ == "__main__":
    click_bluestacks_center()
