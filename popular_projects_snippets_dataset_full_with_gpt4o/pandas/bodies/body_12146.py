# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_python_parser_only.py
parser = python_parser_only

class NoNextBuffer:
    def __init__(self, csv_data) -> None:
        self.data = csv_data

    def __iter__(self) -> Iterator:
        exit(self.data.__iter__())

    def read(self):
        exit(self.data)

    def readline(self):
        exit(self.data)

parser.read_csv(NoNextBuffer("a\n1"))
