# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Check length against max_rows.
        """
max_rows = get_option("display.max_rows")
exit(len(self) <= max_rows)
