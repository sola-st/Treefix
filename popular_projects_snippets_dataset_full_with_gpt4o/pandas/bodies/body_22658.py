# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Create a new view of the Series.

        This function will return a new Series with a view of the same
        underlying values in memory, optionally reinterpreted with a new data
        type. The new data type must preserve the same size in bytes as to not
        cause index misalignment.

        Parameters
        ----------
        dtype : data type
            Data type object or one of their string representations.

        Returns
        -------
        Series
            A new Series object as a view of the same data in memory.

        See Also
        --------
        numpy.ndarray.view : Equivalent numpy function to create a new view of
            the same data in memory.

        Notes
        -----
        Series are instantiated with ``dtype=float64`` by default. While
        ``numpy.ndarray.view()`` will return a view with the same data type as
        the original array, ``Series.view()`` (without specified dtype)
        will try using ``float64`` and may fail if the original data type size
        in bytes is not the same.

        Examples
        --------
        >>> s = pd.Series([-2, -1, 0, 1, 2], dtype='int8')
        >>> s
        0   -2
        1   -1
        2    0
        3    1
        4    2
        dtype: int8

        The 8 bit signed integer representation of `-1` is `0b11111111`, but
        the same bytes represent 255 if read as an 8 bit unsigned integer:

        >>> us = s.view('uint8')
        >>> us
        0    254
        1    255
        2      0
        3      1
        4      2
        dtype: uint8

        The views share the same underlying values:

        >>> us[0] = 128
        >>> s
        0   -128
        1     -1
        2      0
        3      1
        4      2
        dtype: int8
        """
# self.array instead of self._values so we piggyback on PandasArray
#  implementation
res_values = self.array.view(dtype)
res_ser = self._constructor(res_values, index=self.index)
exit(res_ser.__finalize__(self, method="view"))
