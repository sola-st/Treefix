# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# GH 30263
df = DataFrame({"x": date_range("2019", periods=10, tz="UTC")})
expected = repr(df)
df = df.iloc[:, :5]
result = repr(df)
assert result == expected
