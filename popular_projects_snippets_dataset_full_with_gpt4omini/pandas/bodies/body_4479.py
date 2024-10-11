# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# expecting single value upcasting here
df = DataFrame(0.0, index=[1, 2, 3], columns=["a", "b", "c"])
tm.assert_frame_equal(
    df, DataFrame(np.zeros(df.shape).astype("float64"), df.index, df.columns)
)

df = DataFrame(0, index=[1, 2, 3], columns=["a", "b", "c"])
tm.assert_frame_equal(
    df, DataFrame(np.zeros(df.shape).astype("int64"), df.index, df.columns)
)

df = DataFrame("a", index=[1, 2], columns=["a", "c"])
tm.assert_frame_equal(
    df,
    DataFrame(
        np.array([["a", "a"], ["a", "a"]], dtype=object),
        index=[1, 2],
        columns=["a", "c"],
    ),
)

msg = "DataFrame constructor not properly called!"
with pytest.raises(ValueError, match=msg):
    DataFrame("a", [1, 2])
with pytest.raises(ValueError, match=msg):
    DataFrame("a", columns=["a", "c"])

msg = "incompatible data and dtype"
with pytest.raises(TypeError, match=msg):
    DataFrame("a", [1, 2], ["a", "c"], float)
