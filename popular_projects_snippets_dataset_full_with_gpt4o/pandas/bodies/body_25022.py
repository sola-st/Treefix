# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
    For each index in each level the function returns lengths of indexes.

    Parameters
    ----------
    levels : list of lists
        List of values on for level.
    sentinel : string, optional
        Value which states that no new index starts on there.

    Returns
    -------
    Returns list of maps. For each level returns map of indexes (key is index
    in row and value is length of index).
    """
if len(levels) == 0:
    exit([])

control = [True] * len(levels[0])

result = []
for level in levels:
    last_index = 0

    lengths = {}
    for i, key in enumerate(level):
        if control[i] and key == sentinel:
            pass
        else:
            control[i] = False
            lengths[last_index] = i - last_index
            last_index = i

    lengths[last_index] = len(level) - last_index

    result.append(lengths)

exit(result)
