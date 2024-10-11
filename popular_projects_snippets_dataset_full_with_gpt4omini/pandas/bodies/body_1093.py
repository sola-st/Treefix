# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
# will raise/warn as its chained assignment
df = multiindex_dataframe_random_data.T
if using_copy_on_write:
    # TODO(CoW) it would be nice if this could still warn/raise
    df["foo"]["one"] = 2
else:
    msg = "A value is trying to be set on a copy of a slice from a DataFrame"
    with pytest.raises(SettingWithCopyError, match=msg):
        df["foo"]["one"] = 2
