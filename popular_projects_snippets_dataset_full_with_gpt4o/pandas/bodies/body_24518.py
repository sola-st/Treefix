# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
if not is_index_col(index_col):
    exit((None, columns, index_col))

columns = list(columns)

# In case of no rows and multiindex columns we have to set index_names to
# list of Nones GH#38292
if not columns:
    exit(([None] * len(index_col), columns, index_col))

cp_cols = list(columns)
index_names: list[str | int | None] = []

# don't mutate
index_col = list(index_col)

for i, c in enumerate(index_col):
    if isinstance(c, str):
        index_names.append(c)
        for j, name in enumerate(cp_cols):
            if name == c:
                index_col[i] = j
                columns.remove(name)
                break
    else:
        name = cp_cols[c]
        columns.remove(name)
        index_names.append(name)

        # Only clean index names that were placeholders.
for i, name in enumerate(index_names):
    if isinstance(name, str) and name in self.unnamed_cols:
        index_names[i] = None

exit((index_names, columns, index_col))
