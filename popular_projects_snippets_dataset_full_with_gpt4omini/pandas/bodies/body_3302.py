# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_filter.py
# GH13101
df = DataFrame({b"a": [1, 2], b"b": [3, 4]})
expected = DataFrame({b"a": [1, 2]})

tm.assert_frame_equal(df.filter(like=name), expected)
tm.assert_frame_equal(df.filter(regex=name), expected)
