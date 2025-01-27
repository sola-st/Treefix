# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
# calls implementation in pandas/core/base.py
tm.assert_series_equal(ser.transpose(), ser)
