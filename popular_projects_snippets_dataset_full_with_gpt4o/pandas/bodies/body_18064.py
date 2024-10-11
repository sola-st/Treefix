# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_nonkeyword_arguments.py
with tm.assert_produces_warning(None):
    assert g(1, b=3, c=3, d=5) == 12
