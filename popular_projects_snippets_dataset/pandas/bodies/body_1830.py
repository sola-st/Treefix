# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resampler_grouper.py
# GH 26411
df = DataFrame([], columns=["a", "b"], index=TimedeltaIndex([]))
result = df.groupby(keys).resample(rule=pd.to_timedelta("00:00:01")).mean()
expected = (
    DataFrame(columns=["a", "b"])
    .set_index(keys, drop=False)
    .set_index(TimedeltaIndex([]), append=True)
)
if len(keys) == 1:
    expected.index.name = keys[0]

tm.assert_frame_equal(result, expected)
