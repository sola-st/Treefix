# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py
series = Series(constructor("2000-01-01", periods=10, freq="D"))

expected = series.astype("object")

df = DataFrame({"a": series, "b": np.random.randn(len(series))})

result = df.values.squeeze()
assert (result[:, 0] == expected.values).all()

df = DataFrame({"a": series, "b": ["foo"] * len(series)})

result = df.values.squeeze()
assert (result[:, 0] == expected.values).all()
