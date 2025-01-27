# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
category = FutureWarning
match = "Warning"
unmatched = (
    r"Did not see warning 'FutureWarning' matching 'Warning'. "
    r"The emitted warning messages are "
    r"\[FutureWarning\('This is not a match.'\), "
    r"FutureWarning\('Another unmatched warning.'\)\]"
)
with pytest.raises(AssertionError, match=unmatched):
    with tm.assert_produces_warning(category, match=match):
        warnings.warn("This is not a match.", category)
        warnings.warn("Another unmatched warning.", category)
