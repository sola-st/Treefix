# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 21245
s = Series([], index=pd.date_range(start="2018-01-01", periods=0), dtype=int)
result = s.apply(lambda x: x)
tm.assert_series_equal(result, s)
