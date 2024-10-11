# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
# GH 7603
expected = (s.multiply(w).cumsum() / Series(w).cumsum()).fillna(method="ffill")
result = s.ewm(com=2.0, adjust=adjust, ignore_na=ignore_na).mean()

tm.assert_series_equal(result, expected)
if ignore_na is False:
    # check that ignore_na defaults to False
    result = s.ewm(com=2.0, adjust=adjust).mean()
    tm.assert_series_equal(result, expected)
