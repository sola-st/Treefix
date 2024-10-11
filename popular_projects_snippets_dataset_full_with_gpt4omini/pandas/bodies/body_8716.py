# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# GH#24064
dti = self.index_cls(arr1d)

result = dti.round(freq="2T")
expected = dti - pd.Timedelta(minutes=1)
expected = expected._with_freq(None)
tm.assert_index_equal(result, expected)

dta = dti._data
result = dta.round(freq="2T")
expected = expected._data._with_freq(None)
tm.assert_datetime_array_equal(result, expected)
