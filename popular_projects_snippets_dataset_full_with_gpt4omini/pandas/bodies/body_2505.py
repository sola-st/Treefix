# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# `df.A > 6` is a DataFrame with a different shape from df

# boolean with the duplicate raises
df = df_dup_cols
msg = "cannot reindex on an axis with duplicate labels"
with pytest.raises(ValueError, match=msg):
    df[df.A > 6]
