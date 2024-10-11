# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
# we shouldn't raise if comparing tzaware and tznaive datetimes
left = np.array([lvalue], dtype=object)
right = np.array([rvalue], dtype=object)

assert not array_equivalent(left, right, strict_nan=True)
assert not array_equivalent(left, right, strict_nan=False)
