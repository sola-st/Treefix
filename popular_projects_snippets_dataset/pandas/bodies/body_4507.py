# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH21226
class List(list):
    pass

expected = DataFrame([[1, 2, 3], [4, 5, 6]])
result = DataFrame(List([List([1, 2, 3]), List([4, 5, 6])]))
tm.assert_frame_equal(result, expected)
