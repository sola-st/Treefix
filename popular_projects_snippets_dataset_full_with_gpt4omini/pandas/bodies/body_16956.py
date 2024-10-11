# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH#22796
ts = pd.to_datetime([1, 2]).tz_localize("UTC")
a = DataFrame({"A": ts})
b = DataFrame({"A": ts, "B": ts})
result = concat([a, b], sort=True, ignore_index=True)
expected = DataFrame(
    {"A": list(ts) + list(ts), "B": [pd.NaT, pd.NaT] + list(ts)}
)
tm.assert_frame_equal(result, expected)
