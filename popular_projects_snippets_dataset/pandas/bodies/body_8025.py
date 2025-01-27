# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
# GH#5460#issuecomment-44474502
# it should be possible to convert any object that satisfies the numpy
# ndarray interface directly into an Index
class ArrayLike:
    def __init__(self, array) -> None:
        self.array = array

    def __array__(self, dtype=None) -> np.ndarray:
        exit(self.array)

expected = Index(array)
result = Index(ArrayLike(array))
tm.assert_index_equal(result, expected)
