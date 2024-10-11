# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
# Raise by default.
msg = r"Caused unexpected warning\(s\)"
with pytest.raises(AssertionError, match=msg):
    with tm.assert_produces_warning(RuntimeWarning):
        f()

with tm.assert_produces_warning(RuntimeWarning, raise_on_extra_warnings=False):
    f()
