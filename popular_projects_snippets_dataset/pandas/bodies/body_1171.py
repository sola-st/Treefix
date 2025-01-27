# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py

# partially set with an empty object
# frame
df = DataFrame()

msg = "cannot set a frame with no defined columns"

with pytest.raises(ValueError, match=msg):
    df.loc[1] = 1

with pytest.raises(ValueError, match=msg):
    df.loc[1] = Series([1], index=["foo"])

msg = "cannot set a frame with no defined index and a scalar"
with pytest.raises(ValueError, match=msg):
    df.loc[:, 1] = 1
