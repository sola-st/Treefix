# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
assert array_equivalent(
    np.array(["A", "B"], dtype=dtype), np.array(["A", "B"], dtype=dtype)
)
assert not array_equivalent(
    np.array(["A", "B"], dtype=dtype), np.array(["A", "X"], dtype=dtype)
)
