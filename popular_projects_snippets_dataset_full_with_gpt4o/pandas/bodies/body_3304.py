# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_filter.py
# GH#5798 trying to filter on non-string columns should drop,
#  not raise
df = DataFrame(np.random.random((3, 2)), columns=["STRING", 123])
result = df.filter(regex="STRING")
expected = df[["STRING"]]
tm.assert_frame_equal(result, expected)
