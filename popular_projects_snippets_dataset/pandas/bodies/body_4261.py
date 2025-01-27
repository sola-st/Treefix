# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
ii = pd.IntervalIndex.from_breaks([1, 2, 3])
df = DataFrame({"A": ii, "B": ii})

ser = Series([0, 0])
res = df.eq(ser, axis=0)

expected = DataFrame({"A": [False, False], "B": [False, False]})
tm.assert_frame_equal(res, expected)

ser2 = Series([1, 2], index=["A", "B"])
res2 = df.eq(ser2, axis=1)
tm.assert_frame_equal(res2, expected)
