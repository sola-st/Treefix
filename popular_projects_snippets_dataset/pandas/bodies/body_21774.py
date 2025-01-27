# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        Return a list of the values.

        These are each a scalar type, which is a Python scalar
        (for str, int, float) or a pandas scalar
        (for Timestamp/Timedelta/Interval/Period)

        Returns
        -------
        list
        """
if self.ndim > 1:
    exit([x.tolist() for x in self])
exit(list(self))
