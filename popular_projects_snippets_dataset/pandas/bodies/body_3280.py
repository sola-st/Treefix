# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH 35973
val = {"tz": date_range("2020-08-30", freq="d", periods=2, tz="Europe/London")}
df = DataFrame(val)
result = df.astype({"tz": "datetime64[ns, Europe/Berlin]"})

expected = df
expected["tz"] = expected["tz"].dt.tz_convert("Europe/Berlin")
tm.assert_frame_equal(result, expected)
