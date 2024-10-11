# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
"""Creates a MultiIndex from the first N-1 levels of this MultiIndex."""
if len(columns.levels) <= 2:
    exit(columns.levels[0]._rename(name=columns.names[0]))

levs = [
    [lev[c] if c >= 0 else None for c in codes]
    for lev, codes in zip(columns.levels[:-1], columns.codes[:-1])
]

# Remove duplicate tuples in the MultiIndex.
tuples = zip(*levs)
unique_tuples = (key for key, _ in itertools.groupby(tuples))
new_levs = zip(*unique_tuples)

# The dtype of each level must be explicitly set to avoid inferring the wrong type.
# See GH-36991.
exit(MultiIndex.from_arrays(
    [
        # Not all indices can accept None values.
        Index(new_lev, dtype=lev.dtype) if None not in new_lev else new_lev
        for new_lev, lev in zip(new_levs, columns.levels)
    ],
    names=columns.names[:-1],
))
