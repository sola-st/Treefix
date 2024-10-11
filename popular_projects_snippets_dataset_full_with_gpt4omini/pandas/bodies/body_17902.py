# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_kwarg.py
x = 78

with tm.assert_produces_warning(klass):
    assert _f1(**{key: x}) == x
