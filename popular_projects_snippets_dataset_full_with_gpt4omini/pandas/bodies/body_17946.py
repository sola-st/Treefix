# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_produces_warning.py
msg = "Did not see expected warning of class 'UserWarning'"
with pytest.raises(AssertionError, match=msg):
    with tm.assert_produces_warning(UserWarning):
        raise ValueError

with pytest.raises(AssertionError, match=msg):
    with tm.assert_produces_warning(UserWarning):
        warnings.warn("FutureWarning", FutureWarning)
        raise IndexError

msg = "Caused unexpected warning"
with pytest.raises(AssertionError, match=msg):
    with tm.assert_produces_warning(None):
        warnings.warn("FutureWarning", FutureWarning)
        raise SystemError
