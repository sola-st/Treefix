# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
# Still override this for hash_pandas_object
exit((np.asarray(self), self.fill_value))
