# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
path = os.path.join("foo", "bar")
abs_path = os.path.abspath(path)
lpath = LocalPath(path)
assert icom.stringify_path(lpath) == abs_path
