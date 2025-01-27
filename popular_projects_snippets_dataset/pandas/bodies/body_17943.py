# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
msg = r"Caused unexpected warning\(s\)"
with pytest.raises(AssertionError, match=msg):
    with tm.assert_produces_warning(false_or_none):
        f()
