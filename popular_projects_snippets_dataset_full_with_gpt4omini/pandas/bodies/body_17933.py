# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
category = RuntimeWarning
match = "Did not see this warning"
unmatched = (
    r"Did not see warning 'RuntimeWarning' matching 'Did not see this warning'. "
    r"The emitted warning messages are "
    r"\[RuntimeWarning\('This is not a match.'\), "
    r"RuntimeWarning\('Another unmatched warning.'\)\]"
)
with pytest.raises(AssertionError, match=unmatched):
    with tm.assert_produces_warning(category, match=match):
        warnings.warn("This is not a match.", category)
        warnings.warn("Another unmatched warning.", category)
