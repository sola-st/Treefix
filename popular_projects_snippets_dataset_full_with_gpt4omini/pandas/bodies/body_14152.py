# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 16718
df = DataFrame({"a": [0], "b": [1], "c": [2], "d": [3]}).set_index(["a", "b"])
res = df.to_string(header=["r1", "r2"])
exp = "    r1 r2\na b      \n0 1  2  3"
assert res == exp
