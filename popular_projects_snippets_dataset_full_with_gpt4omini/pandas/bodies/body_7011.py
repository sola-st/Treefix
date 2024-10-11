# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_equals.py
# dont raise NotImplementedError when calling is_dtype_compat

mi = MultiIndex.from_arrays([["A", "B", "C", "D"], range(4)])
ci = mi.to_flat_index().astype("category")

assert not ci.equals(mi)
