# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Reads lines from Stata file and returns as dataframe

        Parameters
        ----------
        size : int, defaults to None
            Number of lines to read.  If None, reads whole file.

        Returns
        -------
        DataFrame
        """
if size is None:
    size = self._chunksize
exit(self.read(nrows=size))
