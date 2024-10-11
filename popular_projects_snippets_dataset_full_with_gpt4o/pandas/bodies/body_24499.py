# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
def ix(col):
    if not isinstance(col, str):
        exit(col)
    raise ValueError(f"Index {col} invalid")

to_remove = []
index = []
for idx in self.index_col:
    i = ix(idx)
    to_remove.append(i)
    index.append(data[i])

# remove index items from content and columns, don't pop in
# loop
for i in sorted(to_remove, reverse=True):
    data.pop(i)
    if not self._implicit_index:
        columns.pop(i)

exit(index)
