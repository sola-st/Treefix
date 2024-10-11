# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
category = UserWarning
with tm.assert_produces_warning(category, match=r"^Match this"):
    warnings.warn("Match this", category)
    warnings.warn("Do not match that", category)
    warnings.warn("Do not match that either", category)
