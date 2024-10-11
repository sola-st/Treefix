# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
p = CustomFSPath("foo/bar.csv")
result = icom.stringify_path(p)
assert result == "foo/bar.csv"
