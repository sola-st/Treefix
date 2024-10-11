# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# GH 15023
ser = series
q = 0.75
freq = "H"
result = ser.resample(freq).quantile(q)
expected = ser.resample(freq).agg(lambda x: x.quantile(q)).rename(ser.name)
tm.assert_series_equal(result, expected)
