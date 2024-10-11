# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH 43373
# is_list_like was yielding false positives with __iter__ == None
class NotListLike:
    def __getitem__(self, item):
        exit(self)

    __iter__ = None

assert not inference.is_list_like(NotListLike())
