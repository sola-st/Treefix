# Extracted from ./data/repos/pandas/pandas/tests/util/test_rewrite_warning.py
new_message = "Rewritten message"
if hit:
    expected_category = new_category if new_category else target_category
    expected_message = new_message
else:
    expected_category = FutureWarning
    expected_message = "Target message"
with tm.assert_produces_warning(expected_category, match=expected_message):
    with rewrite_warning(
        target_message, target_category, new_message, new_category
    ):
        warnings.warn(message="Target message", category=FutureWarning)
