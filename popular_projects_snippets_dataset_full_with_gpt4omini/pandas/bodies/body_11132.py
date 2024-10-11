# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 11185
freq = "s"
index = date_range(
    start=Timestamp("2015-09-29T11:34:44-0700"), periods=2, freq=freq
)
df = DataFrame([["A", 10], ["B", 15]], columns=["metric", "values"], index=index)
result = df.groupby([Grouper(level=0, freq=freq), "metric"]).mean()
expected = df.set_index([df.index, "metric"]).astype(float)

tm.assert_frame_equal(result, expected)
