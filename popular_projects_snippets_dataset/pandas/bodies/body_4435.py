# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 32173
arrays = [list("abcd"), list("cdef")]
result = DataFrame([[1, 2, 3, 4], [4, 5, 6, 7]], columns=arrays)

mi = MultiIndex.from_arrays(arrays)
expected = DataFrame([[1, 2, 3, 4], [4, 5, 6, 7]], columns=mi)

tm.assert_frame_equal(result, expected)
