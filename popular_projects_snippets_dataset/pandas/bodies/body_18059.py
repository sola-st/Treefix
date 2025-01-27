# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_nonkeyword_arguments.py
with tm.assert_produces_warning(FutureWarning):
    assert f(6, 3, 3) == 12
