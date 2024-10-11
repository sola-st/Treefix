# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# pre-2.0 this behaved as DataFrame({0: cat}), in 2.0 we remove
#  Categorical special case

df = DataFrame([Categorical(list("abc")), Categorical(list("abd"))])
expected = DataFrame([["a", "b", "c"], ["a", "b", "d"]])
tm.assert_frame_equal(df, expected)
