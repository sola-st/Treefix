# Extracted from ./data/repos/pandas/pandas/io/stata.py
# Check for missing values, and replace if found
replacements = {}
for i, colname in enumerate(data):
    fmt = self.typlist[i]
    if fmt not in self.VALID_RANGE:
        continue

    fmt = cast(str, fmt)  # only strs in VALID_RANGE
    nmin, nmax = self.VALID_RANGE[fmt]
    series = data[colname]

    # appreciably faster to do this with ndarray instead of Series
    svals = series._values
    missing = (svals < nmin) | (svals > nmax)

    if not missing.any():
        continue

    if convert_missing:  # Replacement follows Stata notation
        missing_loc = np.nonzero(np.asarray(missing))[0]
        umissing, umissing_loc = np.unique(series[missing], return_inverse=True)
        replacement = Series(series, dtype=object)
        for j, um in enumerate(umissing):
            missing_value = StataMissingValue(um)

            loc = missing_loc[umissing_loc == j]
            replacement.iloc[loc] = missing_value
    else:  # All replacements are identical
        dtype = series.dtype
        if dtype not in (np.float32, np.float64):
            dtype = np.float64
        replacement = Series(series, dtype=dtype)
        if not replacement._values.flags["WRITEABLE"]:
            # only relevant for ArrayManager; construction
            #  path for BlockManager ensures writeability
            replacement = replacement.copy()
        # Note: operating on ._values is much faster than directly
        # TODO: can we fix that?
        replacement._values[missing] = np.nan
    replacements[colname] = replacement

if replacements:
    for col, value in replacements.items():
        data[col] = value
exit(data)
