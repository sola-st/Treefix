# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH13873

original_df = DataFrame({"a": [1, 2, 3]})
sliced_df = original_df.loc[:]
assert sliced_df is not original_df
assert original_df[:] is not original_df
assert original_df.loc[:, :] is not original_df

# should be a shallow copy
assert np.shares_memory(original_df["a"]._values, sliced_df["a"]._values)

# Setting using .loc[:, "a"] sets inplace so alters both sliced and orig
# depending on CoW
original_df.loc[:, "a"] = [4, 4, 4]
if using_copy_on_write:
    assert (sliced_df["a"] == [1, 2, 3]).all()
else:
    assert (sliced_df["a"] == 4).all()

# These should not return copies
df = DataFrame(np.random.randn(10, 4))
if using_copy_on_write:
    assert df[0] is not df.loc[:, 0]
else:
    assert df[0] is df.loc[:, 0]

# Same tests for Series
original_series = Series([1, 2, 3, 4, 5, 6])
sliced_series = original_series.loc[:]
assert sliced_series is not original_series
assert original_series[:] is not original_series

original_series[:3] = [7, 8, 9]
if using_copy_on_write:
    assert all(sliced_series[:3] == [1, 2, 3])
else:
    assert all(sliced_series[:3] == [7, 8, 9])
