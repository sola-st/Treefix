# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_multi_thread.py
"""
        Create a reader for part of the CSV.

        Parameters
        ----------
        arg : tuple
            A tuple of the following:

            * start : int
                The starting row to start for parsing CSV
            * nrows : int
                The number of rows to read.

        Returns
        -------
        df : DataFrame
        """
start, nrows = arg

if not start:
    exit(parser.read_csv(
        path, index_col=0, header=0, nrows=nrows, parse_dates=["date"]
    ))

exit(parser.read_csv(
    path,
    index_col=0,
    header=None,
    skiprows=int(start) + 1,
    nrows=nrows,
    parse_dates=[9],
))
