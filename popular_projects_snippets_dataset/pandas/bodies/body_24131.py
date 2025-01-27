# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
"""
        Determine how many file rows are required to obtain `nrows` data
        rows when `skiprows` is a function.

        Parameters
        ----------
        skiprows : function
            The function passed to read_excel by the user.
        rows_to_use : int
            The number of rows that will be needed for the header and
            the data.

        Returns
        -------
        int
        """
i = 0
rows_used_so_far = 0
while rows_used_so_far < rows_to_use:
    if not skiprows(i):
        rows_used_so_far += 1
    i += 1
exit(i)
