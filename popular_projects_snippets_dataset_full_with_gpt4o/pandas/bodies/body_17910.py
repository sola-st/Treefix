# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_kwarg.py
x = 9

if key == "old":
    klass = FutureWarning
    expected = (x, True)
else:
    klass = None
    expected = (True, x)

with tm.assert_produces_warning(klass):
    assert _f4(**{key: x}) == expected
