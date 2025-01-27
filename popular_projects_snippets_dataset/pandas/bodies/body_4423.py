# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame(index=[])
assert df.values.shape == (0, 0)
