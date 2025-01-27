# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
"""
        Try several cases to get lines:

        0) There are headers on row 0 and row 1 and their
        total summed lengths equals the length of the next line.
        Treat row 0 as columns and row 1 as indices
        1) Look for implicit index: there are more columns
        on row 1 than row 0. If this is true, assume that row
        1 lists index columns and row 0 lists normal columns.
        2) Get index from the columns if it was listed.
        """
orig_names = list(columns)
columns = list(columns)

line: list[Scalar] | None
if self._header_line is not None:
    line = self._header_line
else:
    try:
        line = self._next_line()
    except StopIteration:
        line = None

next_line: list[Scalar] | None
try:
    next_line = self._next_line()
except StopIteration:
    next_line = None

# implicitly index_col=0 b/c 1 fewer column names
implicit_first_cols = 0
if line is not None:
    # leave it 0, #2442
    # Case 1
    # error: Cannot determine type of 'index_col'
    index_col = self.index_col  # type: ignore[has-type]
    if index_col is not False:
        implicit_first_cols = len(line) - self.num_original_columns

    # Case 0
    if (
        next_line is not None
        and self.header is not None
        and index_col is not False
    ):
        if len(next_line) == len(line) + self.num_original_columns:
            # column and index names on diff rows
            self.index_col = list(range(len(line)))
            self.buf = self.buf[1:]

            for c in reversed(line):
                columns.insert(0, c)

            # Update list of original names to include all indices.
            orig_names = list(columns)
            self.num_original_columns = len(columns)
            exit((line, orig_names, columns))

if implicit_first_cols > 0:
    # Case 1
    self._implicit_index = True
    if self.index_col is None:
        self.index_col = list(range(implicit_first_cols))

    index_name = None

else:
    # Case 2
    (index_name, _, self.index_col) = self._clean_index_names(
        columns, self.index_col
    )

exit((index_name, orig_names, columns))
