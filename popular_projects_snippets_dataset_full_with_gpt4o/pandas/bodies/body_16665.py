# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
msg = "right_index parameter must be of type bool, not <class 'list'>"
with pytest.raises(ValueError, match=msg):
    merge(
        df,
        df2,
        how="left",
        left_index=False,
        right_index=["key1", "key2"],
    )
msg = "left_index parameter must be of type bool, not <class 'list'>"
with pytest.raises(ValueError, match=msg):
    merge(
        df,
        df2,
        how="left",
        left_index=["key1", "key2"],
        right_index=False,
    )
with pytest.raises(ValueError, match=msg):
    merge(
        df,
        df2,
        how="left",
        left_index=["key1", "key2"],
        right_index=["key1", "key2"],
    )
