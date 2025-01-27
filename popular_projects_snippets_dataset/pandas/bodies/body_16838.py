# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# GH 5647
dfa = DataFrame(
    [
        ["2012-08-02", "L", 10],
        ["2012-08-02", "J", 15],
        ["2013-04-06", "L", 20],
        ["2013-04-06", "J", 25],
    ],
    columns=["x", "y", "a"],
)
dfa["x"] = pd.to_datetime(dfa["x"])
dfb = DataFrame(
    [["2012-08-02", "J", 1], ["2013-04-06", "L", 2]],
    columns=["x", "y", "z"],
    index=[2, 4],
)
dfb["x"] = pd.to_datetime(dfb["x"])
result = dfb.join(dfa.set_index(["x", "y"]), on=["x", "y"])
expected = DataFrame(
    [
        [Timestamp("2012-08-02 00:00:00"), "J", 1, 15],
        [Timestamp("2013-04-06 00:00:00"), "L", 2, 20],
    ],
    index=[2, 4],
    columns=["x", "y", "z", "a"],
)
tm.assert_frame_equal(result, expected)
