# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
if usecols is not None and is_integer(x):
    x = usecols[x]

if not is_integer(x):
    x = col_indices[names.index(x)]

exit(x)
