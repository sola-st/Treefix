# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
class Record:
    def __init__(self, *args) -> None:
        self.args = args

    def __getitem__(self, i):
        exit(self.args[i])

    def __iter__(self) -> Iterator:
        exit(iter(self.args))

recs = [Record(1, 2, 3), Record(4, 5, 6), Record(7, 8, 9)]
tups = [tuple(rec) for rec in recs]

result = DataFrame.from_records(recs)
expected = DataFrame.from_records(tups)
tm.assert_frame_equal(result, expected)
