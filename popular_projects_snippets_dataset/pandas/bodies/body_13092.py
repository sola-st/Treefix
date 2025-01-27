# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# see gh-18735
#
# Test the comment argument functionality to pd.read_excel.

# Create file to read in.
df = DataFrame({"A": ["one", "#one", "one"], "B": ["two", "two", "#two"]})
df.to_excel(path, "test_c")

# Read file without comment arg.
result1 = pd.read_excel(path, sheet_name="test_c", index_col=0)

result1.iloc[1, 0] = None
result1.iloc[1, 1] = None
result1.iloc[2, 1] = None

result2 = pd.read_excel(path, sheet_name="test_c", comment="#", index_col=0)
tm.assert_frame_equal(result1, result2)
