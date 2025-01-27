# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#23239
df = DataFrame([values], columns=cols)
df["a"] = df["a"]
result = df["a"].values[0]
assert result == expected
