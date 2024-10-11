# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_numpy_array_equal.py
expected = "Expected type"

with pytest.raises(AssertionError, match=expected):
    tm.assert_numpy_array_equal(1, 2)
