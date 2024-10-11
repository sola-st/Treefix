# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# pre-2.0 this behaved as DataFrame({0: cat}), in 2.0 we remove
#  Categorical special case
# mixed
df = DataFrame([Categorical(list("abc")), list("def")])
expected = DataFrame([["a", "b", "c"], ["d", "e", "f"]])
tm.assert_frame_equal(df, expected)
