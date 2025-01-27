# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame([[1, 2], [3, 4]], dtype="int64")
if not using_array_manager and not using_copy_on_write:
    should_be_view = DataFrame(df.values, dtype=df[0].dtype)
    should_be_view[0][0] = 97
    assert df.values[0, 0] == 97
else:
    # INFO(ArrayManager) DataFrame(ndarray) doesn't necessarily preserve
    # a view on the array to ensure contiguous 1D arrays
    df2 = DataFrame(df.values, dtype=df[0].dtype)
    assert df2._mgr.arrays[0].flags.c_contiguous
