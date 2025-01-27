# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
frame = DataFrame({0: range(3)}, dtype=object)

cat = Categorical(["alpha", "beta", "gamma"])

if not using_array_manager:
    assert frame._mgr.blocks[0]._can_hold_element(cat)

df = frame.copy()
orig_vals = df.values

indexer(df)[key, 0] = cat

expected = DataFrame({0: cat}).astype(object)
if not using_array_manager:
    assert np.shares_memory(df[0].values, orig_vals)

tm.assert_frame_equal(df, expected)

# check we dont have a view on cat (may be undesired GH#39986)
df.iloc[0, 0] = "gamma"
assert cat[0] != "gamma"

# pre-2.0 with mixed dataframe ("split" path) we always overwrote the
#  column.  as of 2.0 we correctly write "into" the column, so
#  we retain the object dtype.
frame = DataFrame({0: np.array([0, 1, 2], dtype=object), 1: range(3)})
df = frame.copy()
orig_vals = df.values
indexer(df)[key, 0] = cat
expected = DataFrame({0: cat.astype(object), 1: range(3)})
tm.assert_frame_equal(df, expected)
