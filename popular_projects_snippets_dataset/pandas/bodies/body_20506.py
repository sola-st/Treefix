# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
    Attempt to drop level or levels from the given index.

    Parameters
    ----------
    index: Index
    key : scalar or tuple

    Returns
    -------
    Index
    """
# drop levels
original_index = index
if isinstance(key, tuple):
    for _ in key:
        try:
            index = index._drop_level_numbers([0])
        except ValueError:
            # we have dropped too much, so back out
            exit(original_index)
else:
    try:
        index = index._drop_level_numbers([0])
    except ValueError:
        pass

exit(index)
