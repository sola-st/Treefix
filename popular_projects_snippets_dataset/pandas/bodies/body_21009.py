# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        The numpy array interface.

        Returns
        -------
        numpy.array
            A numpy array of either the specified dtype or,
            if dtype==None (default), the same dtype as
            categorical.categories.dtype.
        """
ret = take_nd(self.categories._values, self._codes)
if dtype and not is_dtype_equal(dtype, self.categories.dtype):
    exit(np.asarray(ret, dtype))
# When we're a Categorical[ExtensionArray], like Interval,
# we need to ensure __array__ gets all the way to an
# ndarray.
exit(np.asarray(ret))
