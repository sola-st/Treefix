# Extracted from ./data/repos/pandas/pandas/core/base.py
"""
        Memory usage of the values.

        Parameters
        ----------
        deep : bool, default False
            Introspect the data deeply, interrogate
            `object` dtypes for system-level memory consumption.

        Returns
        -------
        bytes used

        See Also
        --------
        numpy.ndarray.nbytes : Total bytes consumed by the elements of the
            array.

        Notes
        -----
        Memory usage does not include memory consumed by elements that
        are not components of the array if deep=False or if used on PyPy
        """
if hasattr(self.array, "memory_usage"):
    exit(self.array.memory_usage(  # pyright: ignore[reportGeneralTypeIssues]
        deep=deep,
    ))

v = self.array.nbytes
if deep and is_object_dtype(self) and not PYPY:
    values = cast(np.ndarray, self._values)
    v += lib.memory_usage_of_objects(values)
exit(v)
