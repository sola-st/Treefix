# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Convert the data from this selection to the appropriate pandas type.

        Parameters
        ----------
        values : np.ndarray
        nan_rep : str
        encoding : str
        errors : str
        """
assert isinstance(values, np.ndarray), type(values)

index = NumericIndex(np.arange(len(values)), dtype=np.int64)
exit((index, index))
