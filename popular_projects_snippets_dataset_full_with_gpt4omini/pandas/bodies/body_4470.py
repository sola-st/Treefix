# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 9232 validation

s0 = Series(range(5), name=0)
s1 = Series(range(5), name=1)

# matching name and column gives standard frame
tm.assert_frame_equal(DataFrame(s0, columns=[0]), s0.to_frame())
tm.assert_frame_equal(DataFrame(s1, columns=[1]), s1.to_frame())

# non-matching produces empty frame
assert DataFrame(s0, columns=[1]).empty
assert DataFrame(s1, columns=[0]).empty
