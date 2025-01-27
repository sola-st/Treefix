# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
df = multiindex_df.rename_axis("A")
df = df.set_flags(allows_duplicate_labels=flag)

msg = r"cannot insert \('A', ''\), already exists"
with pytest.raises(ValueError, match=msg):
    df.reset_index()
