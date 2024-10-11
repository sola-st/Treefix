# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py
df = DataFrame([[1, 2.5], [3, 4.5]], index=[1, 2], columns=["x", "x"])
result = df.values
expected = np.array([[1, 2.5], [3, 4.5]])
assert (result == expected).all().all()
