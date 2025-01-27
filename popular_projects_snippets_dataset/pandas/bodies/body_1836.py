# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py

r = test_series.resample("H")
assert (
    "DatetimeIndexResampler [freq=<Hour>, axis=0, closed=left, "
    "label=left, convention=start, origin=start_day]" in str(r)
)

r = test_series.resample("H", origin="2000-01-01")
assert (
    "DatetimeIndexResampler [freq=<Hour>, axis=0, closed=left, "
    "label=left, convention=start, origin=2000-01-01 00:00:00]" in str(r)
)
