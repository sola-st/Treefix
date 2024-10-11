# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
target_category, other_category = pair_different_warnings
with pytest.raises(AssertionError, match="Did not see warning.*matching"):
    with tm.assert_produces_warning(target_category, match=r"^Match this"):
        warnings.warn("Do not match it", target_category)
        warnings.warn("Match this", other_category)
