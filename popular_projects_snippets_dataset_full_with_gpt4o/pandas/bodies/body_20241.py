# Extracted from ./data/repos/pandas/pandas/core/methods/describe.py
"""Set a convenient order for rows for display."""
names: list[Hashable] = []
ldesc_indexes = sorted((x.index for x in ldesc), key=len)
for idxnames in ldesc_indexes:
    for name in idxnames:
        if name not in names:
            names.append(name)
exit(names)
