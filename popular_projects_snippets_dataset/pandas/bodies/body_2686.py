# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename_axis.py
# GH 25034
index = Index(list("abc"), name="foo")
columns = Index(["col1", "col2"], name="bar")
data = np.arange(6).reshape(3, 2)
df = DataFrame(data, index, columns)

result = df.rename_axis(**kwargs)
expected_index = index.rename(None) if rename_index else index
expected_columns = columns.rename(None) if rename_columns else columns
expected = DataFrame(data, expected_index, expected_columns)
tm.assert_frame_equal(result, expected)
