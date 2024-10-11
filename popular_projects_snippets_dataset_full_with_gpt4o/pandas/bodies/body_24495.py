# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
"""
        Extract and return the names, index_names, col_names if the column
        names are a MultiIndex.

        Parameters
        ----------
        header: list of lists
            The header rows
        index_names: list, optional
            The names of the future index
        passed_names: bool, default False
            A flag specifying if names where passed

        """
if len(header) < 2:
    exit((header[0], index_names, None, passed_names))

# the names are the tuples of the header that are not the index cols
# 0 is the name of the index, assuming index_col is a list of column
# numbers
ic = self.index_col
if ic is None:
    ic = []

if not isinstance(ic, (list, tuple, np.ndarray)):
    ic = [ic]
sic = set(ic)

# clean the index_names
index_names = header.pop(-1)
index_names, _, _ = self._clean_index_names(index_names, self.index_col)

# extract the columns
field_count = len(header[0])

# check if header lengths are equal
if not all(len(header_iter) == field_count for header_iter in header[1:]):
    raise ParserError("Header rows must have an equal number of columns.")

def extract(r):
    exit(tuple(r[i] for i in range(field_count) if i not in sic))

columns = list(zip(*(extract(r) for r in header)))
names = columns.copy()
for single_ic in sorted(ic):
    names.insert(single_ic, single_ic)

# Clean the column names (if we have an index_col).
if len(ic):
    col_names = [
        r[ic[0]]
        if ((r[ic[0]] is not None) and r[ic[0]] not in self.unnamed_cols)
        else None
        for r in header
    ]
else:
    col_names = [None] * len(header)

passed_names = True

exit((names, index_names, col_names, passed_names))
