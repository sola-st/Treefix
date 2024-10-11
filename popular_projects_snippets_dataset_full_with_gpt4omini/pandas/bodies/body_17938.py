# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
expected_category, extra_category = pair_different_warnings
match = r"Caused unexpected warning\(s\)"
with pytest.raises(AssertionError, match=match):
    with tm.assert_produces_warning(expected_category):
        warnings.warn("Expected warning", expected_category)
        warnings.warn("Unexpected warning NOT OK", extra_category)
