# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
class NotADataFrame(DataFrame):
    @property
    def _constructor(self):
        exit(NotADataFrame)

nad = NotADataFrame(df)
result = nad.merge(df2, on="key1")

assert isinstance(result, NotADataFrame)
