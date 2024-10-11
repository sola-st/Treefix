# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_tz_localize.py
rng = date_range("1/1/2011", periods=100, freq="H")

df = DataFrame({"a": 1}, index=rng)

df = df.T
result = df.tz_localize("utc", axis=1)
assert result.columns.tz is timezone.utc

expected = DataFrame({"a": 1}, rng.tz_localize("UTC"))

tm.assert_frame_equal(result, expected.T)
