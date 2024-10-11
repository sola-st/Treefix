# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
result = isna(value)
if is_scalar(result):
    assert result is expected
else:
    tm.assert_numpy_array_equal(result, expected)
