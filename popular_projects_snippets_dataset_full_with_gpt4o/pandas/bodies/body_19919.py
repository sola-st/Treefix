# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
        Index with indexers that should return an object of the same dimension
        as self.obj.

        This is only called after a failed call to _getitem_lowerdim.
        """
retval = self.obj
for i, key in enumerate(tup):
    if com.is_null_slice(key):
        continue

    retval = getattr(retval, self.name)._getitem_axis(key, axis=i)
    # We should never have retval.ndim < self.ndim, as that should
    #  be handled by the _getitem_lowerdim call above.
    assert retval.ndim == self.ndim

if retval is self.obj:
    # if all axes were a null slice (`df.loc[:, :]`), ensure we still
    # return a new object (https://github.com/pandas-dev/pandas/pull/49469)
    retval = retval.copy(deep=False)

exit(retval)
