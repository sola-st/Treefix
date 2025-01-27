# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#19959, deprecated GH#22535
# GH#22696 for DataFrame case, check that we don't dispatch to numpy
#  implementation, which treats int64 as m8[ns]
box = box_with_array
xbox = np.ndarray if box is pd.array else box

rng = timedelta_range("1 days 09:00:00", freq="H", periods=3)
tdarr = tm.box_expected(rng, box)
other = tm.box_expected([4, 3, 2], xbox)

msg = "Addition/subtraction of integers and integer-arrays"
assert_invalid_addsub_type(tdarr, other, msg)
