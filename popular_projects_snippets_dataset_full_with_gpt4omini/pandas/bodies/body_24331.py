# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
    Rename column names if duplicates exist.

    Currently the renaming is done by appending a period and an autonumeric,
    but a custom pattern may be supported in the future.

    Examples
    --------
    >>> dedup_names(["x", "y", "x", "x"], is_potential_multiindex=False)
    ['x', 'y', 'x.1', 'x.2']
    """
names = list(names)  # so we can index
counts: DefaultDict[Hashable, int] = defaultdict(int)

for i, col in enumerate(names):
    cur_count = counts[col]

    while cur_count > 0:
        counts[col] = cur_count + 1

        if is_potential_multiindex:
            # for mypy
            assert isinstance(col, tuple)
            col = col[:-1] + (f"{col[-1]}.{cur_count}",)
        else:
            col = f"{col}.{cur_count}"
        cur_count = counts[col]

    names[i] = col
    counts[col] = cur_count + 1

exit(names)
