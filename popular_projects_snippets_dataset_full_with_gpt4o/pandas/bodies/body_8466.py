# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_freq_attr.py
# Setting the freq for one DatetimeIndex shouldn't alter the freq
#  for another that views the same data

dti = date_range("2016-01-01", periods=5)
dta = dti._data

dti2 = DatetimeIndex(dta)._with_freq(None)
assert dti2.freq is None

# Original was not altered
assert dti.freq == "D"
assert dta.freq == "D"
