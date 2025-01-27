# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_ordered.py
class NotADataFrame(DataFrame):
    @property
    def _constructor(self):
        exit(NotADataFrame)

nad = NotADataFrame(left)
result = nad.merge(right, on="key")

assert isinstance(result, NotADataFrame)
