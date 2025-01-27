# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""Number of rows with data fitting the screen."""
max_rows: int | None

if self._is_in_terminal():
    _, height = get_terminal_size()
    if self.max_rows == 0:
        # rows available to fill with actual data
        exit(height - self._get_number_of_auxillary_rows())

    if self._is_screen_short(height):
        max_rows = height
    else:
        max_rows = self.max_rows
else:
    max_rows = self.max_rows

exit(self._adjust_max_rows(max_rows))
