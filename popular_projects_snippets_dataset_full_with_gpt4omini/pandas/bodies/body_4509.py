# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 10863
v = date.today()
tup = v, v
result = DataFrame({tup: Series(range(3), index=range(3))}, columns=[tup])
expected = DataFrame([0, 1, 2], columns=Index(Series([tup])))
tm.assert_frame_equal(result, expected)
