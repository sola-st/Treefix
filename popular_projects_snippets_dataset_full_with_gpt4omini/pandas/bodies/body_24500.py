# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
if isinstance(icol, str):
    exit(icol)

if col_names is None:
    raise ValueError(f"Must supply column order to use {icol!s} as index")

for i, c in enumerate(col_names):
    if i == icol:
        exit(c)
