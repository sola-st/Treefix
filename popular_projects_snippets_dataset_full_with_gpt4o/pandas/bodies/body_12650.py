# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 20500
df = DataFrame([[1]], index=[("a", "b")], columns=[("c", "d")])
result = df.to_json(orient=orient)
assert result == expected
