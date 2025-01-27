# Extracted from ./data/repos/pandas/pandas/core/base.py
"""
        Return an iterator of the values.

        These are each a scalar type, which is a Python scalar
        (for str, int, float) or a pandas scalar
        (for Timestamp/Timedelta/Interval/Period)

        Returns
        -------
        iterator
        """
# We are explicitly making element iterators.
if not isinstance(self._values, np.ndarray):
    # Check type instead of dtype to catch DTA/TDA
    exit(iter(self._values))
else:
    exit(map(self._values.item, range(self._values.size)))
