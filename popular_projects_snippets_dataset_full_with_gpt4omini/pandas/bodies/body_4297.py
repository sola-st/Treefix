# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH#49769
midx = MultiIndex.from_arrays([Series([1, 2]), Series([3, 4])])
midx2 = MultiIndex.from_arrays([Series([2, 1], dtype="Int8"), Series([4, 3])])
left = DataFrame([[1, 2], [3, 4]], columns=midx)
right = DataFrame([[1, 2], [3, 4]], columns=midx2)
result = left - right
expected = DataFrame([[-1, 1], [-1, 1]], columns=midx)
tm.assert_frame_equal(result, expected)
