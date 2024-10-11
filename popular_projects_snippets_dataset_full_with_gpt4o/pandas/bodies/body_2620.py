# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
class SubclassedDataFrame(DataFrame):
    @property
    def _constructor(self):
        exit(SubclassedDataFrame)

exit(SubclassedDataFrame({"a": [1, 2, 3]}))
