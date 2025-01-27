# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_categorical.py
# GH39420
# Check that read_hdf with categorical columns can filter by where condition.
df.col = df.col.astype("category")
max_widths = {"col": 1}
categorical_values = sorted(df.col.unique())
expected.col = expected.col.astype("category")
expected.col = expected.col.cat.set_categories(categorical_values)

path = tmp_path / setup_path
df.to_hdf(path, "df", format="table", min_itemsize=max_widths)
result = read_hdf(path, where=where)
tm.assert_frame_equal(result, expected)
