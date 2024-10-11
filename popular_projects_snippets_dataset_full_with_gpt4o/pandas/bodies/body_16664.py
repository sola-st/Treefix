# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
msg = "Must pass right_on or right_index=True"
with pytest.raises(pd.errors.MergeError, match=msg):
    merge(left, right, left_index=True)
msg = "Must pass left_on or left_index=True"
with pytest.raises(pd.errors.MergeError, match=msg):
    merge(left, right, right_index=True)

msg = (
    'Can only pass argument "on" OR "left_on" and "right_on", not '
    "a combination of both"
)
with pytest.raises(pd.errors.MergeError, match=msg):
    merge(left, left, left_on="key", on="key")

msg = r"len\(right_on\) must equal len\(left_on\)"
with pytest.raises(ValueError, match=msg):
    merge(df, df2, left_on=["key1"], right_on=["key1", "key2"])
