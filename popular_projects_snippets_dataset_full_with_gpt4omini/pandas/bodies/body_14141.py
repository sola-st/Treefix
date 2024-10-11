# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
s = Series(range(10), dtype="int64")
with option_context("display.max_rows", 1):
    strrepr = repr(s).split("\n")
exp1 = ["0", "0"]
res1 = strrepr[0].split()
assert exp1 == res1
exp2 = [".."]
res2 = strrepr[1].split()
assert exp2 == res2
