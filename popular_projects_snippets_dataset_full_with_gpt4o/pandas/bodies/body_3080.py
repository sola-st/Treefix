# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_duplicated.py
# gh-21524
# Given the wide dataframe with a lot of columns
# with different (important!) values
data = {f"col_{i:02d}": np.random.randint(0, 1000, 30000) for i in range(100)}
df = DataFrame(data).T
result = df.duplicated()

# Then duplicates produce the bool Series as a result and don't fail during
# calculation. Actual values doesn't matter here, though usually it's all
# False in this case
assert isinstance(result, Series)
assert result.dtype == np.bool_
