# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
rng = TimedeltaIndex(["1 days", NaT, "2 days"])
mismatched = [1, 2, 3, 4]

rng = tm.box_expected(rng, box_with_array)
msg = "Cannot divide vectors|Unable to coerce to Series"
for obj in [mismatched, mismatched[:2]]:
    # one shorter, one longer
    for other in [obj, np.array(obj), pd.Index(obj)]:
        with pytest.raises(ValueError, match=msg):
            rng / other
        with pytest.raises(ValueError, match=msg):
            other / rng
