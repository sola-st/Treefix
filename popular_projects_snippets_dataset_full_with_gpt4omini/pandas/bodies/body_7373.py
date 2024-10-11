# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_timedelta.py
index = pd.to_timedelta(range(5), unit="d")._with_freq("infer")
assert index.freq == "D"
ret = index + pd.offsets.Hour(1)
assert ret.freq == "D"
exit(ret)
