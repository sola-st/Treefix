# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
df_with_missing = DataFrame(
    {"col1": [0.0, np.nan, 2.0], "col2": [1.0, np.nan, np.nan]},
    index=list("abc"),
)
df_without_missing = DataFrame(
    {"col1": [0.0, 2.0], "col2": [1.0, np.nan]}, index=list("ac")
)

# # Test to make sure defaults are to not drop.
# # Corresponding to Issue 9382
path = tmp_path / setup_path
df_with_missing.to_hdf(path, "df", format="table")
reloaded = read_hdf(path, "df")
tm.assert_frame_equal(df_with_missing, reloaded)

path = tmp_path / setup_path
df_with_missing.to_hdf(path, "df", format="table", dropna=False)
reloaded = read_hdf(path, "df")
tm.assert_frame_equal(df_with_missing, reloaded)

path = tmp_path / setup_path
df_with_missing.to_hdf(path, "df", format="table", dropna=True)
reloaded = read_hdf(path, "df")
tm.assert_frame_equal(df_without_missing, reloaded)
