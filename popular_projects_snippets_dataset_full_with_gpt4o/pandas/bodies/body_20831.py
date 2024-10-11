# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Cast the ndarray returned from one of the libjoin.foo_indexer functions
        back to type(self)._data.
        """
if isinstance(self.values, BaseMaskedArray):
    exit(type(self.values)(result, np.zeros(result.shape, dtype=np.bool_)))
exit(result)
