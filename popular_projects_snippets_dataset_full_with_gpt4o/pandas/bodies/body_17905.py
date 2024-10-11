# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_kwarg.py
with tm.assert_produces_warning(FutureWarning):
    assert _f3(old=x) == _f3_mapping(x)
