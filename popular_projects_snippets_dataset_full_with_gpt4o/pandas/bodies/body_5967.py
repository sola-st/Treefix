# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
# Bypass NumPy's shape inference to get a (N,) array of tuples.
frozen = [tuple(x.items()) for x in self]
exit(construct_1d_object_array_from_listlike(frozen))
