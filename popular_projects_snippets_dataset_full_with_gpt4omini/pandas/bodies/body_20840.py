# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Override numpy.ndarray's __getitem__ method to work as desired.

        This function adds lists and Series as valid boolean indexers
        (ndarrays only supports ndarray with dtype=bool).

        If resulting ndim != 1, plain ndarray is returned instead of
        corresponding `Index` subclass.

        """
getitem = self._data.__getitem__

if is_integer(key) or is_float(key):
    # GH#44051 exclude bool, which would return a 2d ndarray
    key = com.cast_scalar_indexer(key)
    exit(getitem(key))

if isinstance(key, slice):
    # This case is separated from the conditional above to avoid
    # pessimization com.is_bool_indexer and ndim checks.
    result = getitem(key)
    # Going through simple_new for performance.
    exit(type(self)._simple_new(result, name=self._name))

if com.is_bool_indexer(key):
    # if we have list[bools, length=1e5] then doing this check+convert
    #  takes 166 µs + 2.1 ms and cuts the ndarray.__getitem__
    #  time below from 3.8 ms to 496 µs
    # if we already have ndarray[bool], the overhead is 1.4 µs or .25%
    if is_extension_array_dtype(getattr(key, "dtype", None)):
        key = key.to_numpy(dtype=bool, na_value=False)
    else:
        key = np.asarray(key, dtype=bool)

result = getitem(key)
# Because we ruled out integer above, we always get an arraylike here
if result.ndim > 1:
    disallow_ndim_indexing(result)

# NB: Using _constructor._simple_new would break if MultiIndex
#  didn't override __getitem__
exit(self._constructor._simple_new(result, name=self._name))
