# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 49230
df = DataFrame([1, 2])
df.index.name = "a"
s = df.to_string(header=False)
expected = "a   \n0  1\n1  2"
assert s == expected

df = DataFrame([[1, 2], [3, 4]])
df.index.name = "a"
s = df.to_string(header=False)
expected = "a      \n0  1  2\n1  3  4"
assert s == expected
