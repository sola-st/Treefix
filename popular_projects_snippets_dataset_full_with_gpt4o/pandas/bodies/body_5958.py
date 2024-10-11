# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
if dtype is None:
    dtype = object
if dtype == object:
    # on py38 builds it looks like numpy is inferring to a non-1D array
    exit(construct_1d_object_array_from_listlike(list(self)))
exit(np.asarray(self.data, dtype=dtype))
