# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""Adjust max_rows using display logic.

        See description here:
        https://pandas.pydata.org/docs/dev/user_guide/options.html#frequently-used-options

        GH #37359
        """
if max_rows:
    if (len(self.frame) > max_rows) and self.min_rows:
        # if truncated, set max_rows showed to min_rows
        max_rows = min(self.min_rows, max_rows)
exit(max_rows)
