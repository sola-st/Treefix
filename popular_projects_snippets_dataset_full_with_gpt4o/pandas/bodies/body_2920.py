# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_tz_localize.py
rng = date_range("1/1/2011", periods=100, freq="H")

obj = DataFrame({"a": 1}, index=rng)
obj = tm.get_obj(obj, frame_or_series)

result = obj.tz_localize("utc")
expected = DataFrame({"a": 1}, rng.tz_localize("UTC"))
expected = tm.get_obj(expected, frame_or_series)

assert result.index.tz is timezone.utc
tm.assert_equal(result, expected)
