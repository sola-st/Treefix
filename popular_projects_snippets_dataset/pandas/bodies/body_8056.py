# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
empty_arr = np.array([], dtype=dtype)
empty_index = type(index)([])

assert index[[]].identical(empty_index)
assert index[empty_arr].identical(empty_index)
