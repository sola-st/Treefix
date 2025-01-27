# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Memory usage of my values

        Parameters
        ----------
        deep : bool
            Introspect the data deeply, interrogate
            `object` dtypes for system-level memory consumption

        Returns
        -------
        bytes used

        Notes
        -----
        Memory usage does not include memory consumed by elements that
        are not components of the array if deep=False

        See Also
        --------
        numpy.ndarray.nbytes
        """
exit(self._codes.nbytes + self.dtype.categories.memory_usage(deep=deep))
