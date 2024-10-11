# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# make sure we can compare Timestamps on the right AND left hand side
# GH#4982
df = DataFrame(
    {
        "dates1": pd.date_range("20010101", periods=10),
        "dates2": pd.date_range("20010102", periods=10),
        "intcol": np.random.randint(1000000000, size=10),
        "floatcol": np.random.randn(10),
        "stringcol": list(tm.rands(10)),
    }
)
df.loc[np.random.rand(len(df)) > 0.5, "dates2"] = pd.NaT
left_f = getattr(operator, left)
right_f = getattr(operator, right)

# no nats
if left in ["eq", "ne"]:
    expected = left_f(df, pd.Timestamp("20010109"))
    result = right_f(pd.Timestamp("20010109"), df)
    tm.assert_frame_equal(result, expected)
else:
    msg = (
        "'(<|>)=?' not supported between "
        "instances of 'numpy.ndarray' and 'Timestamp'"
    )
    with pytest.raises(TypeError, match=msg):
        left_f(df, pd.Timestamp("20010109"))
    with pytest.raises(TypeError, match=msg):
        right_f(pd.Timestamp("20010109"), df)
        # nats
if left in ["eq", "ne"]:
    expected = left_f(df, pd.Timestamp("nat"))
    result = right_f(pd.Timestamp("nat"), df)
    tm.assert_frame_equal(result, expected)
else:
    msg = (
        "'(<|>)=?' not supported between "
        "instances of 'numpy.ndarray' and 'NaTType'"
    )
    with pytest.raises(TypeError, match=msg):
        left_f(df, pd.Timestamp("nat"))
    with pytest.raises(TypeError, match=msg):
        right_f(pd.Timestamp("nat"), df)
