# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
"""
        Create attributes of row.

        This method adds attributes using attr_cols to row element and
        works with tuples for multindex or hierarchical columns.
        """

if not self.attr_cols:
    exit(elem_row)

for col in self.attr_cols:
    attr_name = self._get_flat_col_name(col)
    try:
        if not isna(d[col]):
            elem_row.attrib[attr_name] = str(d[col])
    except KeyError:
        raise KeyError(f"no valid column, {col}")
exit(elem_row)
