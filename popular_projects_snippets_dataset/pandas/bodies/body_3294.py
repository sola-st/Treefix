# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_tz_convert.py
rng = date_range("1/1/2011", periods=200, freq="D", tz="US/Eastern")

obj = DataFrame({"a": 1}, index=rng)
obj = tm.get_obj(obj, frame_or_series)

result = obj.tz_convert("Europe/Berlin")
expected = DataFrame({"a": 1}, rng.tz_convert("Europe/Berlin"))
expected = tm.get_obj(expected, frame_or_series)

assert result.index.tz.zone == "Europe/Berlin"
tm.assert_equal(result, expected)
