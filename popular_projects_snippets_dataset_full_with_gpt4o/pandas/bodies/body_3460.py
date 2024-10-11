# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# GH 11479
idx = range(3)
tstamp = date_range("2015-07-01", freq="D", periods=3)
df = DataFrame({"id": idx, "tstamp": tstamp, "a": list("abc")})
df.loc[2, "tstamp"] = pd.NaT
result = df.set_index(["id", "tstamp"]).reset_index("id")
expected = DataFrame(
    {"id": range(3), "a": list("abc")},
    index=pd.DatetimeIndex(["2015-07-01", "2015-07-02", "NaT"], name="tstamp"),
)
tm.assert_frame_equal(result, expected)
