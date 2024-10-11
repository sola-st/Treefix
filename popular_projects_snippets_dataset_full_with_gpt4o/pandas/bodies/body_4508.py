# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH11363
expected = DataFrame(Series(extension_arr))
result = DataFrame(extension_arr)
tm.assert_frame_equal(result, expected)
