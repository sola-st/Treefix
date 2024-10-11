# Extracted from ./data/repos/pandas/pandas/io/formats/html.py
if self.fmt.index:
    # showing (row) index
    exit(self.frame.index.nlevels)
elif self.show_col_idx_names:
    # see gh-22579
    # Column misalignment also occurs for
    # a standard index when the columns index is named.
    # If the row index is not displayed a column of
    # blank cells need to be included before the DataFrame values.
    exit(1)
# not showing (row) index
exit(0)
