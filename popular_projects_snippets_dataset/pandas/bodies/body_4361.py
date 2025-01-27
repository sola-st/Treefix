# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#9232
x = Series(range(5), name=1)
y = Series(range(5), name=0)

result = DataFrame(x, columns=[0])
expected = DataFrame([], columns=[0])
tm.assert_frame_equal(result, expected)

result = DataFrame(y, columns=[1])
expected = DataFrame([], columns=[1])
tm.assert_frame_equal(result, expected)
