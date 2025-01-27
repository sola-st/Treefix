# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# Re issue #18735
# Test the comment argument default to pd.read_excel

# Create file to read in
df = DataFrame({"A": ["one", "#one", "one"], "B": ["two", "two", "#two"]})
df.to_excel(path, "test_c")

# Read file with default and explicit comment=None
result1 = pd.read_excel(path, sheet_name="test_c")
result2 = pd.read_excel(path, sheet_name="test_c", comment=None)
tm.assert_frame_equal(result1, result2)
