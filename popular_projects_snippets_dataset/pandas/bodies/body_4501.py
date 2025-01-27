# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame([Categorical(list("abc")), Categorical(list("abdefg"))])
expected = DataFrame([list("abc"), list("abdefg")])
tm.assert_frame_equal(df, expected)
