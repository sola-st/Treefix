# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
df = DataFrame({"A": [2, 3]})
assert df.attrs == {}
df.attrs["version"] = 1

result = df.rename(columns=str)
assert result.attrs == {"version": 1}
