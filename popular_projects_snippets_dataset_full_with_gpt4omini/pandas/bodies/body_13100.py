# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-13347
df = DataFrame([["foo", "bar"]], columns=["col1", "col2"])
expected = df.replace({"foo": True, "bar": False})

df.to_excel(path)
read_frame = pd.read_excel(
    path, true_values=["foo"], false_values=["bar"], index_col=0
)
tm.assert_frame_equal(read_frame, expected)
