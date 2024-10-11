# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/39272
arr = np.array(["a", "b"], dtype="object")
df = DataFrame(arr)
assert np.shares_memory(df.values, arr)
