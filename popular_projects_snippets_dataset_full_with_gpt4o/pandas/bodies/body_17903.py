# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_kwarg.py
with tm.assert_produces_warning(FutureWarning):
    assert _f2(old=key) == _f2_mappings[key]
