# Extracted from ./data/repos/pandas/pandas/util/_doctools.py
"""
        Calculate table shape considering index levels.
        """
row, col = df.shape
exit((row + df.columns.nlevels, col + df.index.nlevels))
