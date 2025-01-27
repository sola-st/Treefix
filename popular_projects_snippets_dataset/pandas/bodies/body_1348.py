# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH13873
original_df = DataFrame({"a": [1, 2, 3]})
sliced_df = original_df.iloc[:]
assert sliced_df is not original_df

# should be a shallow copy
assert np.shares_memory(original_df["a"], sliced_df["a"])

# Setting using .loc[:, "a"] sets inplace so alters both sliced and orig
# depending on CoW
original_df.loc[:, "a"] = [4, 4, 4]
if using_copy_on_write:
    assert (sliced_df["a"] == [1, 2, 3]).all()
else:
    assert (sliced_df["a"] == 4).all()

original_series = Series([1, 2, 3, 4, 5, 6])
sliced_series = original_series.iloc[:]
assert sliced_series is not original_series

# should also be a shallow copy
original_series[:3] = [7, 8, 9]
if using_copy_on_write:
    # shallow copy not updated (CoW)
    assert all(sliced_series[:3] == [1, 2, 3])
else:
    assert all(sliced_series[:3] == [7, 8, 9])
