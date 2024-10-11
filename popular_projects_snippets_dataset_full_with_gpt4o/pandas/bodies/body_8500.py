# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
dti = date_range("20130101", periods=3, tz="US/Eastern")

tail = dti[2:].tolist()
i2 = Index([pd.NaT, pd.NaT] + tail)

mask = notna(i2)

# passing tz-naive ndarray to tzaware DTI
result = dti.where(mask, i2.values)
expected = Index([pd.NaT.asm8, pd.NaT.asm8] + tail, dtype=object)
tm.assert_index_equal(result, expected)

# passing tz-aware DTI to tznaive DTI
naive = dti.tz_localize(None)
result = naive.where(mask, i2)
expected = Index([i2[0], i2[1]] + naive[2:].tolist(), dtype=object)
tm.assert_index_equal(result, expected)

pi = i2.tz_localize(None).to_period("D")
result = dti.where(mask, pi)
expected = Index([pi[0], pi[1]] + tail, dtype=object)
tm.assert_index_equal(result, expected)

tda = i2.asi8.view("timedelta64[ns]")
result = dti.where(mask, tda)
expected = Index([tda[0], tda[1]] + tail, dtype=object)
assert isinstance(expected[0], np.timedelta64)
tm.assert_index_equal(result, expected)

result = dti.where(mask, i2.asi8)
expected = Index([pd.NaT.value, pd.NaT.value] + tail, dtype=object)
assert isinstance(expected[0], int)
tm.assert_index_equal(result, expected)

# non-matching scalar
td = pd.Timedelta(days=4)
result = dti.where(mask, td)
expected = Index([td, td] + tail, dtype=object)
assert expected[0] is td
tm.assert_index_equal(result, expected)
