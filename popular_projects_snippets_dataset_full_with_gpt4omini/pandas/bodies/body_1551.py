# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# Test that data type is preserved . GH#5782
df = DataFrame({"one": np.arange(6, dtype=np.int8)})
df.loc[1, "one"] = 6
assert df.dtypes.one == np.dtype(np.int8)
df.one = np.int8(7)
assert df.dtypes.one == np.dtype(np.int8)
