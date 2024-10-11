# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-5235
df = DataFrame([[1, 2, 3], [1, 2, 3], [1, 2, 3]], columns=["A", "B", "B"])
df.to_excel(path, "test1")
expected = DataFrame(
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]], columns=["A", "B", "B.1"]
)

# By default, we mangle.
result = pd.read_excel(path, sheet_name="test1", index_col=0)
tm.assert_frame_equal(result, expected)

# see gh-11007, gh-10970
df = DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]], columns=["A", "B", "A", "B"])
df.to_excel(path, "test1")

result = pd.read_excel(path, sheet_name="test1", index_col=0)
expected = DataFrame(
    [[1, 2, 3, 4], [5, 6, 7, 8]], columns=["A", "B", "A.1", "B.1"]
)
tm.assert_frame_equal(result, expected)

# see gh-10982
df.to_excel(path, "test1", index=False, header=False)
result = pd.read_excel(path, sheet_name="test1", header=None)

expected = DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]])
tm.assert_frame_equal(result, expected)
