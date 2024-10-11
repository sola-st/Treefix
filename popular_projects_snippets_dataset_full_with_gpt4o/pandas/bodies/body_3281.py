# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH 35973
val = {"tz": date_range("2020-08-30", freq="d", periods=2, tz="Europe/London")}
expected = DataFrame(val)

# convert expected to object dtype from other tz str (independently tested)
result = expected.astype({"tz": f"datetime64[ns, {tz}]"})
result = result.astype({"tz": "object"})

# do real test: object dtype to a specified tz, different from construction tz.
result = result.astype({"tz": "datetime64[ns, Europe/London]"})
tm.assert_frame_equal(result, expected)
