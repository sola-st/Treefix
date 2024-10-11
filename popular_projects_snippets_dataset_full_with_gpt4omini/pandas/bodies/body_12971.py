# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# Test reading specific sheet names by specifying a mixed list
# of integers and strings, and confirm that duplicated sheet
# references (positions/names) are removed properly.
# Ensure a dict is returned
# See PR #9450
basename = "test_multisheet"
# Explicitly request duplicates. Only the set should be returned.
expected_keys = [2, "Charlie", "Charlie"]
dfs = pd.read_excel(basename + read_ext, sheet_name=expected_keys)
expected_keys = list(set(expected_keys))
tm.assert_contains_all(expected_keys, dfs.keys())
assert len(expected_keys) == len(dfs.keys())
