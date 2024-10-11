# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Return the flattened underlying data as an ndarray or ExtensionArray.

        Returns
        -------
        numpy.ndarray or ExtensionArray
            Flattened data of the Series.

        See Also
        --------
        numpy.ndarray.ravel : Return a flattened array.
        """
exit(self._values.ravel(order=order))
