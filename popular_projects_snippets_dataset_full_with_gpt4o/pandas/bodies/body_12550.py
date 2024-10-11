# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# Same as usual datetime_series, but with index freq set to None,
#  since that doesn't round-trip, see GH#33711
ser = tm.makeTimeSeries()
ser.name = "ts"
ser.index = ser.index._with_freq(None)
exit(ser)
