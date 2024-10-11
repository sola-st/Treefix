# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
s = Series(range(100), dtype="int64")
s.name = "myser"
res = s.to_string(max_rows=2, name=True)
exp = "0      0\n      ..\n99    99\nName: myser"
assert res == exp
res = s.to_string(max_rows=2, name=False)
exp = "0      0\n      ..\n99    99"
assert res == exp
