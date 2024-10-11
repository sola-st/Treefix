# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
# GH 10741
df1 = DataFrame(
    [
        ["a", "x", 0.471780],
        ["a", "y", 0.774908],
        ["a", "z", 0.563634],
        ["b", "x", -0.353756],
        ["b", "y", 0.368062],
        ["b", "z", -1.721840],
        ["c", "x", 1],
        ["c", "y", 2],
        ["c", "z", 3],
    ],
    columns=["first", "second", "value1"],
).set_index(["first", "second"])

df2 = DataFrame([["a", 10], ["b", 20]], columns=["first", "value2"]).set_index(
    ["first"]
)

exp = DataFrame(
    [
        [0.471780, 10],
        [0.774908, 10],
        [0.563634, 10],
        [-0.353756, 20],
        [0.368062, 20],
        [-1.721840, 20],
        [1.000000, np.nan],
        [2.000000, np.nan],
        [3.000000, np.nan],
    ],
    index=df1.index,
    columns=["value1", "value2"],
)

# these must be the same results (but columns are flipped)
tm.assert_frame_equal(df1.join(df2, how="left"), exp)
tm.assert_frame_equal(df2.join(df1, how="right"), exp[["value2", "value1"]])

exp_idx = MultiIndex.from_product(
    [["a", "b"], ["x", "y", "z"]], names=["first", "second"]
)
exp = DataFrame(
    [
        [0.471780, 10],
        [0.774908, 10],
        [0.563634, 10],
        [-0.353756, 20],
        [0.368062, 20],
        [-1.721840, 20],
    ],
    index=exp_idx,
    columns=["value1", "value2"],
)

tm.assert_frame_equal(df1.join(df2, how="right"), exp)
tm.assert_frame_equal(df2.join(df1, how="left"), exp[["value2", "value1"]])
