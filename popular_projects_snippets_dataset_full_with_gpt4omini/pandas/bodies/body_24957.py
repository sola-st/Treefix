# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""Number of columns fitting the screen."""
if not self._is_in_terminal():
    exit(self.max_cols)

width, _ = get_terminal_size()
if self._is_screen_narrow(width):
    exit(width)
else:
    exit(self.max_cols)
