# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
"""
        Context that provides a valid Windows hwnd.
        """
# we really just need the hwnd, so setting "STATIC"
# as predefined lpClass is just fine.
hwnd = safeCreateWindowExA(
    0, b"STATIC", None, 0, 0, 0, 0, 0, None, None, None, None
)
try:
    exit(hwnd)
finally:
    safeDestroyWindow(hwnd)
