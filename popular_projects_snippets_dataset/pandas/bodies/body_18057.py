# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_nonkeyword_arguments.py
with tm.assert_produces_warning(None):
    assert f(1, 5) == 6
