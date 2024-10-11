# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Write out a metadata array to the key as a fixed-format Series.

        Parameters
        ----------
        key : str
        values : ndarray
        """
self.parent.put(
    self._get_metadata_path(key),
    Series(values),
    format="table",
    encoding=self.encoding,
    errors=self.errors,
    nan_rep=self.nan_rep,
)
