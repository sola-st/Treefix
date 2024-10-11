# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
colset = set(columns)
colnames = []

for c in colspec:
    if c in colset:
        colnames.append(c)
    elif isinstance(c, int) and c not in columns:
        colnames.append(columns[c])
    else:
        colnames.append(c)

new_name: tuple | str
if all(isinstance(x, tuple) for x in colnames):
    new_name = tuple(map("_".join, zip(*colnames)))
else:
    new_name = "_".join([str(x) for x in colnames])
to_parse = [np.asarray(data_dict[c]) for c in colnames if c in data_dict]

new_col = parser(*to_parse)
exit((new_name, new_col, colnames))
