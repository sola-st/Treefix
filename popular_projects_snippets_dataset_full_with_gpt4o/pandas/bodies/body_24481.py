# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
"""
        Read rows from self.f, skipping as specified.

        We distinguish buffer_rows (the first <= infer_nrows
        lines) from the rows returned to detect_colspecs
        because it's simpler to leave the other locations
        with skiprows logic alone than to modify them to
        deal with the fact we skipped some rows here as
        well.

        Parameters
        ----------
        infer_nrows : int
            Number of rows to read from self.f, not counting
            rows that are skipped.
        skiprows: set, optional
            Indices of rows to skip.

        Returns
        -------
        detect_rows : list of str
            A list containing the rows to read.

        """
if skiprows is None:
    skiprows = set()
buffer_rows = []
detect_rows = []
for i, row in enumerate(self.f):
    if i not in skiprows:
        detect_rows.append(row)
    buffer_rows.append(row)
    if len(detect_rows) >= infer_nrows:
        break
self.buffer = iter(buffer_rows)
exit(detect_rows)
