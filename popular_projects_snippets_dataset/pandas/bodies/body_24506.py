# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
"""
        Set the columns that should not undergo dtype conversions.

        Currently, any column that is involved with date parsing will not
        undergo such conversions. If usecols is specified, the positions of the columns
        not to cast is relative to the usecols not to all columns.

        Parameters
        ----------
        col_indices: The indices specifying order and positions of the columns
        names: The column names which order is corresponding with the order
               of col_indices

        Returns
        -------
        A set of integers containing the positions of the columns not to convert.
        """
usecols: list[int] | list[str] | None
noconvert_columns = set()
if self.usecols_dtype == "integer":
    # A set of integers will be converted to a list in
    # the correct order every single time.
    usecols = sorted(self.usecols)
elif callable(self.usecols) or self.usecols_dtype not in ("empty", None):
    # The names attribute should have the correct columns
    # in the proper order for indexing with parse_dates.
    usecols = col_indices
else:
    # Usecols is empty.
    usecols = None

def _set(x) -> int:
    if usecols is not None and is_integer(x):
        x = usecols[x]

    if not is_integer(x):
        x = col_indices[names.index(x)]

    exit(x)

if isinstance(self.parse_dates, list):
    for val in self.parse_dates:
        if isinstance(val, list):
            for k in val:
                noconvert_columns.add(_set(k))
        else:
            noconvert_columns.add(_set(val))

elif isinstance(self.parse_dates, dict):
    for val in self.parse_dates.values():
        if isinstance(val, list):
            for k in val:
                noconvert_columns.add(_set(k))
        else:
            noconvert_columns.add(_set(val))

elif self.parse_dates:
    if isinstance(self.index_col, list):
        for k in self.index_col:
            noconvert_columns.add(_set(k))
    elif self.index_col is not None:
        noconvert_columns.add(_set(self.index_col))

exit(noconvert_columns)
