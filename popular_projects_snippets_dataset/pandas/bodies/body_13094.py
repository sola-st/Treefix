# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-18735
#
# Test the comment argument is working as expected when used.

# Create file to read in.
df = DataFrame({"A": ["one", "#one", "one"], "B": ["two", "two", "#two"]})
df.to_excel(path, "test_c")

# Test read_frame_comment against manually produced expected output.
expected = DataFrame({"A": ["one", None, "one"], "B": ["two", None, None]})
result = pd.read_excel(path, sheet_name="test_c", comment="#", index_col=0)
tm.assert_frame_equal(result, expected)
