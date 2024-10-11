# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_ordered.py
# GH 9157
with pytest.raises(ValueError, match=pattern):
    pd.concat(df_seq)
