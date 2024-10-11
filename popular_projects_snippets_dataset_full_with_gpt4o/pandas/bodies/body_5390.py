# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
if method is Timestamp.round:
    diff = np.abs((res - ts).value)
    assert diff <= nanos / 2
elif method is Timestamp.floor:
    assert res <= ts
elif method is Timestamp.ceil:
    assert res >= ts
