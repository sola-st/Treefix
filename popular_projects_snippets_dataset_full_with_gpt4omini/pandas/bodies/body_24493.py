# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
if isinstance(self.parse_dates, bool):
    exit(self.parse_dates)
else:
    if self.index_names is not None:
        name = self.index_names[i]
    else:
        name = None
    j = i if self.index_col is None else self.index_col[i]

    if is_scalar(self.parse_dates):
        exit((j == self.parse_dates) or (
            name is not None and name == self.parse_dates
        ))
    else:
        exit((j in self.parse_dates) or (
            name is not None and name in self.parse_dates
        ))
