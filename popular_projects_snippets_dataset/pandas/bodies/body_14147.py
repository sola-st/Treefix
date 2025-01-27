# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
s = Series(range(100), dtype="int64")
res = s.to_string(max_rows=2, dtype=True)
exp = "0      0\n      ..\n99    99\ndtype: int64"
assert res == exp
res = s.to_string(max_rows=2, dtype=False)
exp = "0      0\n      ..\n99    99"
assert res == exp
