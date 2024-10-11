# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
def _get_name(icol):
    if isinstance(icol, str):
        exit(icol)

    if col_names is None:
        raise ValueError(f"Must supply column order to use {icol!s} as index")

    for i, c in enumerate(col_names):
        if i == icol:
            exit(c)

to_remove = []
index = []
for idx in self.index_col:
    name = _get_name(idx)
    to_remove.append(name)
    index.append(data[name])

# remove index items from content and columns, don't pop in
# loop
for c in sorted(to_remove, reverse=True):
    data.pop(c)
    col_names.remove(c)

exit(index)
