# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH 12396

# tz-naive
first = DataFrame([[pd.NaT], [pd.NaT]]).apply(lambda x: x.dt.tz_localize(tz1))
second = DataFrame([s]).apply(lambda x: x.dt.tz_localize(tz2))

result = concat([first, second], axis=0)
expected = DataFrame(Series([pd.NaT, pd.NaT, s], index=[0, 1, 0]))
expected = expected.apply(lambda x: x.dt.tz_localize(tz2))
if tz1 != tz2:
    expected = expected.astype(object)

tm.assert_frame_equal(result, expected)
