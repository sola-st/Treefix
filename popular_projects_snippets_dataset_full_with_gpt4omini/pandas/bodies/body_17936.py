# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
expected_category, actual_category = pair_different_warnings
match = "Did not see expected warning of class"
with pytest.raises(AssertionError, match=match):
    with tm.assert_produces_warning(expected_category):
        warnings.warn("warning message", actual_category)
