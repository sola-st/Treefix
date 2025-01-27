# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
tuples = list(product(["foo", "bar"], [10, 20], [1.0, 1.1]))
index = MultiIndex.from_tuples(tuples, names=["prm0", "prm1", "prm2"])
df = DataFrame(np.random.randn(8, 3), columns=["A", "B", "C"], index=index)
deleveled = df.reset_index()
assert is_integer_dtype(deleveled["prm1"])
assert is_float_dtype(deleveled["prm2"])
