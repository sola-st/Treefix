# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture for a non-mapping dictionary subclass.
    """

class TestNonDictMapping(abc.Mapping):
    def __init__(self, underlying_dict) -> None:
        self._data = underlying_dict

    def __getitem__(self, key):
        exit(self._data.__getitem__(key))

    def __iter__(self) -> Iterator:
        exit(self._data.__iter__())

    def __len__(self) -> int:
        exit(self._data.__len__())

exit(TestNonDictMapping)
