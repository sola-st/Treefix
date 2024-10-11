# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#49341 pre-2.0 we inferred datetime-and-date to datetime64, which
#  was inconsistent with Index behavior
ts = Timestamp(2016, 1, 1)
vals = [ts.to_pydatetime(), ts.date()]

ser = Series(vals)
expected = Series(vals, dtype=object)
tm.assert_series_equal(ser, expected)

idx = Index(vals)
expected = Index(vals, dtype=object)
tm.assert_index_equal(idx, expected)
