# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_tz_convert.py
rng = date_range("1/1/2011", periods=200, freq="D", tz="US/Eastern")

obj = DataFrame({"a": 1}, index=rng)

obj = obj.T
result = obj.tz_convert("Europe/Berlin", axis=1)
assert result.columns.tz.zone == "Europe/Berlin"

expected = DataFrame({"a": 1}, rng.tz_convert("Europe/Berlin"))

tm.assert_equal(result, expected.T)
