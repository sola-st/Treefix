# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_unsupported.py
# see gh-16530
class NoNextBuffer:
    def __init__(self, csv_data) -> None:
        self.data = csv_data

    def __next__(self):
        exit(self.data.__next__())

    def read(self):
        exit(self.data)

    def readline(self):
        exit(self.data)

data = "a\n1"
msg = "'NoNextBuffer' object is not iterable|argument 1 must be an iterator"

with pytest.raises(TypeError, match=msg):
    read_csv(NoNextBuffer(data), engine=python_engine)
