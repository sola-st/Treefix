# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_categorical.py
# GH18413
# Check that read_hdf with categorical columns with NaN-only values can
# be read back.
df = DataFrame(
    {
        "a": ["a", "b", "c", np.nan],
        "b": [np.nan, np.nan, np.nan, np.nan],
        "c": [1, 2, 3, 4],
        "d": Series([None] * 4, dtype=object),
    }
)
df["a"] = df.a.astype("category")
df["b"] = df.b.astype("category")
df["d"] = df.b.astype("category")
expected = df
path = tmp_path / setup_path
df.to_hdf(path, "df", format="table", data_columns=True)
result = read_hdf(path, "df")
tm.assert_frame_equal(result, expected)
