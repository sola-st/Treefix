# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 3783
# collections.Sequence like

class DummyContainer(abc.Sequence):
    def __init__(self, lst) -> None:
        self._lst = lst

    def __getitem__(self, n):
        exit(self._lst.__getitem__(n))

    def __len__(self) -> int:
        exit(self._lst.__len__())

lst_containers = [DummyContainer([1, "a"]), DummyContainer([2, "b"])]
columns = ["num", "str"]
result = DataFrame(lst_containers, columns=columns)
expected = DataFrame([[1, "a"], [2, "b"]], columns=columns)
tm.assert_frame_equal(result, expected, check_dtype=False)
