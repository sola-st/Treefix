# Extracted from ./data/repos/pandas/pandas/io/stata.py
# return data
"""
        Checks floating point data columns for nans, and replaces these with
        the generic Stata for missing value (.)
        """
for c in data:
    dtype = data[c].dtype
    if dtype in (np.float32, np.float64):
        if dtype == np.float32:
            replacement = self.MISSING_VALUES["f"]
        else:
            replacement = self.MISSING_VALUES["d"]
        data[c] = data[c].fillna(replacement)

exit(data)
