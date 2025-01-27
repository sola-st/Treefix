# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 18338
df = DataFrame(
    {
        "timestamp": [pd.Timestamp("2017-08-27 01:00:00.709949+0000", tz="UTC")],
        "a": ["a"],
        "b": ["b"],
        "c": ["c"],
    },
    columns=["timestamp", "a", "b", "c"],
)
result = df.set_index(["a", "b"]).unstack()
expected = DataFrame(
    [[pd.Timestamp("2017-08-27 01:00:00.709949+0000", tz="UTC"), "c"]],
    index=Index(["a"], name="a"),
    columns=MultiIndex(
        levels=[["timestamp", "c"], ["b"]],
        codes=[[0, 1], [0, 0]],
        names=[None, "b"],
    ),
)
tm.assert_frame_equal(result, expected)
