# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
df1 = tm.makeTimeDataFrame()
df2 = tm.makeTimeDataFrame()

row = simple_frame.xs("a")
ndim_5 = np.ones(df1.shape + (1, 1, 1))

result = func(df1, df2)
tm.assert_numpy_array_equal(result.values, func(df1.values, df2.values))

msg = (
    "Unable to coerce to Series/DataFrame, "
    "dimension must be <= 2: (30, 4, 1, 1, 1)"
)
with pytest.raises(ValueError, match=re.escape(msg)):
    func(df1, ndim_5)

result2 = func(simple_frame, row)
tm.assert_numpy_array_equal(
    result2.values, func(simple_frame.values, row.values)
)

result3 = func(float_frame, 0)
tm.assert_numpy_array_equal(result3.values, func(float_frame.values, 0))

msg = (
    r"Can only compare identically-labeled \(both index and columns\) "
    "DataFrame objects"
)
with pytest.raises(ValueError, match=msg):
    func(simple_frame, simple_frame[:2])
