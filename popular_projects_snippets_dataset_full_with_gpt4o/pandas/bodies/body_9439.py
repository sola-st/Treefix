# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
# https://github.com/pandas-dev/pandas/pull/32867
# ensure the integers are not cast to float during reductions
df = pd.DataFrame({"a": pd.array([1, 2], dtype="Int64")})
result = df.max()
assert isinstance(result["a"], np.int64)
