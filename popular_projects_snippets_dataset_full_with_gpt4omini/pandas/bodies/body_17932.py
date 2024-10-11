# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
with tm.assert_produces_warning(category, match=match):
    warnings.warn(message, category)
