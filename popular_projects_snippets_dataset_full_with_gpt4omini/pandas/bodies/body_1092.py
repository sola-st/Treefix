# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
# this works because we are modifying the underlying array
# really a no-no
df = multiindex_dataframe_random_data.T
df["foo"].values[:] = 0
assert (df["foo"].values == 0).all()
