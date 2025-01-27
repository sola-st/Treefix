# Extracted from ./data/repos/pandas/pandas/tests/resample/test_timedelta.py
# GH #12169
df = DataFrame({"Group_obj": "A"}, index=pd.to_timedelta(list(range(20)), unit="s"))
df["Group"] = df["Group_obj"].astype("category")
result = df.resample("10s").agg(lambda x: (x.value_counts().index[0]))
expected = DataFrame(
    {"Group_obj": ["A", "A"], "Group": ["A", "A"]},
    index=pd.TimedeltaIndex([0, 10], unit="s", freq="10s"),
)
expected = expected.reindex(["Group_obj", "Group"], axis=1)
expected["Group"] = expected["Group_obj"]
tm.assert_frame_equal(result, expected)
