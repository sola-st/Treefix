# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
# https://github.com/pandas-dev/pandas/issues/47829
category = (FutureWarning, UserWarning)
with tm.assert_produces_warning(category, match=r"^Match this"):
    warnings.warn("Match this", FutureWarning)
    warnings.warn("Match this too", UserWarning)
