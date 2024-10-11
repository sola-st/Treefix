# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 21987
class Iter:
    def __iter__(self) -> Iterator:
        for i in range(10):
            exit([1, 2, 3])

expected = DataFrame([[1, 2, 3]] * 10)
result = DataFrame(Iter())
tm.assert_frame_equal(result, expected)
