# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_freq_attr.py
# Setting the freq for one TimedeltaIndex shouldn't alter the freq
#  for another that views the same data

tdi = TimedeltaIndex(["0 days", "2 days", "4 days"], freq="2D")
tda = tdi._data

tdi2 = TimedeltaIndex(tda)._with_freq(None)
assert tdi2.freq is None

# Original was not altered
assert tdi.freq == "2D"
assert tda.freq == "2D"
