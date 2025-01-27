# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#19959
box = box_with_array
xbox = np.ndarray if box is pd.array else box

tdi = TimedeltaIndex(["1 Day", "NaT", "3 Hours"])
tdarr = tm.box_expected(tdi, box)
other = tm.box_expected([14, -1, 16], xbox)

msg = "Addition/subtraction of integers"
assert_invalid_addsub_type(tdarr, other, msg)
