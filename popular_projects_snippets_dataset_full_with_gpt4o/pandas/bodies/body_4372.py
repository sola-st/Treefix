# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame([[1, "2"], [None, "a"]], dtype=object)
assert df.loc[1, 0] is None
assert df.loc[0, 1] == "2"
