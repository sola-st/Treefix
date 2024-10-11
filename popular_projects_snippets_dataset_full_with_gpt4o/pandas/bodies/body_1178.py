# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# GH#5756
# setting with empty Series
df = DataFrame(Series(dtype=object))
expected = DataFrame({0: Series(dtype=object)})
tm.assert_frame_equal(df, expected)

df = DataFrame(Series(name="foo", dtype=object))
expected = DataFrame({"foo": Series(dtype=object)})
tm.assert_frame_equal(df, expected)
