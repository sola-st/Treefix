# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_almost_equal.py
msg = "expected 2\\.00000 but got 1\\.00000, with rtol=1e-05, atol=1e-08"

with pytest.raises(AssertionError, match=msg):
    tm.assert_almost_equal(1, 2)
