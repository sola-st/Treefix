# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_period.py
dti = date_range("1/1/2000", "1/7/2002", freq="B")
pi = dti.to_period()
tm.assert_index_equal(pi.to_timestamp(), dti)

dti = date_range("1/1/2000", "1/7/2002", freq="B")
pi = dti.to_period(freq="H")
tm.assert_index_equal(pi.to_timestamp(), dti)
