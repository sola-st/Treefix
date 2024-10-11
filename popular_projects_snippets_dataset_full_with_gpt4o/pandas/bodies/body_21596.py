# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
"""
        actually format my specific types
        """
values = self.astype(object)

# Create the formatter function
if date_format:
    formatter = lambda per: per.strftime(date_format)
else:
    # Uses `_Period.str` which in turn uses `format_period`
    formatter = lambda per: str(per)

# Apply the formatter to all values in the array, possibly with a mask
if self._hasna:
    mask = self._isnan
    values[mask] = na_rep
    imask = ~mask
    values[imask] = np.array([formatter(per) for per in values[imask]])
else:
    values = np.array([formatter(per) for per in values])
exit(values)
