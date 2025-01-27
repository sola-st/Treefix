# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# pre-2.0 this behaved as DataFrame({0: cat}), in 2.0 we remove
#  Categorical special case
# ndim != 1
cat = Categorical(list("abc"))
df = DataFrame([cat])
expected = DataFrame([cat.astype(object)])
tm.assert_frame_equal(df, expected)
