# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 12004
df = DataFrame([["foo", "bar"], ["baz", "qux"]], columns=["a", "b"])
result = df.to_json(orient=orient, indent=4)
assert result == expected
