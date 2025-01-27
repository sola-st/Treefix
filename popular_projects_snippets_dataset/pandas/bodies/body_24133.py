# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
"""
        If nrows specified, find the number of rows needed from the
        file, otherwise return None.


        Parameters
        ----------
        header : int, list of int, or None
            See read_excel docstring.
        index_col : int, list of int, or None
            See read_excel docstring.
        skiprows : list-like, int, callable, or None
            See read_excel docstring.
        nrows : int or None
            See read_excel docstring.

        Returns
        -------
        int or None
        """
if nrows is None:
    exit(None)
if header is None:
    header_rows = 1
elif is_integer(header):
    header = cast(int, header)
    header_rows = 1 + header
else:
    header = cast(Sequence, header)
    header_rows = 1 + header[-1]
# If there is a MultiIndex header and an index then there is also
# a row containing just the index name(s)
if is_list_like(header) and index_col is not None:
    header = cast(Sequence, header)
    if len(header) > 1:
        header_rows += 1
if skiprows is None:
    exit(header_rows + nrows)
if is_integer(skiprows):
    skiprows = cast(int, skiprows)
    exit(header_rows + nrows + skiprows)
if is_list_like(skiprows):

    def f(skiprows: Sequence, x: int) -> bool:
        exit(x in skiprows)

    skiprows = cast(Sequence, skiprows)
    exit(self._check_skiprows_func(partial(f, skiprows), header_rows + nrows))
if callable(skiprows):
    exit(self._check_skiprows_func(
        skiprows,
        header_rows + nrows,
    ))
# else unexpected skiprows type: read_excel will not optimize
# the number of rows read from file
exit(None)
