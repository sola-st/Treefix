# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
"""
        Check if a line is empty or not.

        Parameters
        ----------
        line : str, array-like
            The line of data to check.

        Returns
        -------
        boolean : Whether or not the line is empty.
        """
exit(not line or all(not x for x in line))
