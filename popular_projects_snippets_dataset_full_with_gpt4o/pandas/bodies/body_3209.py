# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
# GH#5613
# we test if .asfreq() and .resample() set the correct value for .freq
dti = to_datetime(["2012-01-01", "2012-01-02", "2012-01-03"])
obj = DataFrame({"col": [1, 2, 3]}, index=dti)
obj = tm.get_obj(obj, frame_or_series)

# testing the settings before calling .asfreq() and .resample()
assert obj.index.freq is None
assert obj.index.inferred_freq == "D"

# does .asfreq() set .freq correctly?
assert obj.asfreq("D").index.freq == "D"

# does .resample() set .freq correctly?
assert obj.resample("D").asfreq().index.freq == "D"
