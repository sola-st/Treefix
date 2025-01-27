# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-34331
df = DataFrame({"render": [1, 2], "data": [3, 4]})
df.to_excel(path, "Sheet1")
read = pd.read_excel(path, "Sheet1", index_col=0)
expected = df
tm.assert_frame_equal(read, expected)
