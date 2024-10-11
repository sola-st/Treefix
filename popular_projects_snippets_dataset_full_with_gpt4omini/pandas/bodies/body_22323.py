# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Adjust our binner when upsampling.

        The range of a new index should not be outside specified range
        """
if self.closed == "right":
    binner = binner[1:]
else:
    binner = binner[:-1]
exit(binner)
