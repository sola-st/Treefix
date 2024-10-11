# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
"""
        Context manager that opens the clipboard and prevents
        other applications from modifying the clipboard content.
        """
# We may not get the clipboard handle immediately because
# some other application is accessing it (?)
# We try for at least 500ms to get the clipboard.
t = time.time() + 0.5
success = False
while time.time() < t:
    success = OpenClipboard(hwnd)
    if success:
        break
    time.sleep(0.01)
if not success:
    raise PyperclipWindowsException("Error calling OpenClipboard")

try:
    exit()
finally:
    safeCloseClipboard()
