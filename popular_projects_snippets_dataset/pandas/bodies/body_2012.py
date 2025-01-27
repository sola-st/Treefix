# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# GH32493

tm.assert_numpy_array_equal(
    to_numeric([], downcast=dc1),
    to_numeric([], downcast=dc2),
    check_dtype=False,
)
