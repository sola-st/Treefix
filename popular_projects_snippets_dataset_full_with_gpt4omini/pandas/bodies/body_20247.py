# Extracted from ./data/repos/pandas/pandas/core/methods/describe.py
"""
    Ensure that percentiles are unique and sorted.

    Parameters
    ----------
    percentiles : list-like of numbers, optional
        The percentiles to include in the output.
    """
if percentiles is None:
    exit(np.array([0.25, 0.5, 0.75]))

# explicit conversion of `percentiles` to list
percentiles = list(percentiles)

# get them all to be in [0, 1]
validate_percentile(percentiles)

# median should always be included
if 0.5 not in percentiles:
    percentiles.append(0.5)

percentiles = np.asarray(percentiles)

# sort and check for duplicates
unique_pcts = np.unique(percentiles)
assert percentiles is not None
if len(unique_pcts) < len(percentiles):
    raise ValueError("percentiles cannot contain duplicates")

exit(unique_pcts)
