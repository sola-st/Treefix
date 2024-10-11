# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
kurt = nanops.nankurt(samples)
tm.assert_almost_equal(kurt, actual_kurt)
