# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH#46149 avoid unnecessary copies
arr = np.full((40, 50), np.nan)
df = DataFrame(arr)

df[0].fillna(-1, inplace=True)
if using_copy_on_write:
    assert np.isnan(arr[:, 0]).all()
else:
    assert (arr[:, 0] == -1).all()

# i.e. we didn't create a new 49-column block
assert len(df._mgr.arrays) == 1
assert np.shares_memory(df.values, arr)
