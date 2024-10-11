# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_scalar_compat.py
# GH#17157
index = period_range(freq="M", start="2016-01-01", end="2016-05-31")
expected_index = date_range("2016-01-01", end="2016-05-31", freq="MS")
tm.assert_index_equal(index.start_time, expected_index)
