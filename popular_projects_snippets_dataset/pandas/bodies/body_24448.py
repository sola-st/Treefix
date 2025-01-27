# Extracted from ./data/repos/pandas/pandas/io/parsers/c_parser_wrapper.py
"""
        Set the columns that should not undergo dtype conversions.

        Currently, any column that is involved with date parsing will not
        undergo such conversions.
        """
assert self.orig_names is not None
# error: Cannot determine type of 'names'

# much faster than using orig_names.index(x) xref GH#44106
names_dict = {x: i for i, x in enumerate(self.orig_names)}
col_indices = [names_dict[x] for x in self.names]  # type: ignore[has-type]
# error: Cannot determine type of 'names'
noconvert_columns = self._set_noconvert_dtype_columns(
    col_indices,
    self.names,  # type: ignore[has-type]
)
for col in noconvert_columns:
    self._reader.set_noconvert(col)
