# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH#12701
idx = Index([2, 3, 4, 4, 5], name="id")
idxdt = pd.to_datetime(
    [
        "2016-03-23 14:00",
        "2016-03-23 15:00",
        "2016-03-23 16:00",
        "2016-03-23 16:00",
        "2016-03-23 17:00",
    ]
)
df = DataFrame(np.arange(10).reshape(5, 2), columns=list("ab"), index=idx)
df["tstamp"] = idxdt
df = df.set_index("tstamp", append=True)
ts = Timestamp("201603231600")
assert df.index.is_unique is False

result = df.drop(ts, level="tstamp")
expected = df.loc[idx != 4]
tm.assert_frame_equal(result, expected)
