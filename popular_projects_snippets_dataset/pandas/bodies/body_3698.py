# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# Check that corr does not lead to incorrect entries in item_cache

df = DataFrame({"A": range(10)})
df["B"] = range(10)[::-1]

ser = df["A"]  # populate item_cache
assert len(df._mgr.arrays) == 2  # i.e. 2 blocks

_ = df.corr(numeric_only=True)

if using_copy_on_write:
    # TODO(CoW) we should disallow this, so `df` doesn't get updated
    ser.values[0] = 99
    assert df.loc[0, "A"] == 99
else:
    # Check that the corr didn't break link between ser and df
    ser.values[0] = 99
    assert df.loc[0, "A"] == 99
    assert df["A"] is ser
    assert df.values[0, 0] == 99
