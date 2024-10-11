# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
# GH#12358
# tz-aware Series should retain the tz
idx = DatetimeIndex(["2014-01-01 10:10:10"], tz="UTC").tz_convert("Europe/Rome")
df = DataFrame({"A": idx})
assert df.set_index(idx).index[0].hour == 11
assert DatetimeIndex(Series(df.A))[0].hour == 11
assert df.set_index(df.A).index[0].hour == 11
