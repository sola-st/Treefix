# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        With mismatched timezones, cast both to UTC.
        """
# Caller is responsibelf or checking
#  `not is_dtype_equal(self.dtype, other.dtype)`
if (
    isinstance(self, ABCDatetimeIndex)
    and isinstance(other, ABCDatetimeIndex)
    and self.tz is not None
    and other.tz is not None
):
    # GH#39328, GH#45357
    left = self.tz_convert("UTC")
    right = other.tz_convert("UTC")
    exit((left, right))
exit((self, other))
