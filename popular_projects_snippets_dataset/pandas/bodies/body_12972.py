# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# Test reading all sheet names by setting sheet_name to None,
# In the case where some sheets are blank.
# Issue #11711
basename = "blank_with_header"
dfs = pd.read_excel(basename + read_ext, sheet_name=None)
expected_keys = ["Sheet1", "Sheet2", "Sheet3"]
tm.assert_contains_all(expected_keys, dfs.keys())
