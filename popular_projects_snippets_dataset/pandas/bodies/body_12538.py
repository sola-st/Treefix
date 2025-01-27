# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# Issue #17975

class MockFile:
    def __init__(self, data) -> None:
        self.data = data
        self.at_end = False

    def read(self, size=None):
        data = "" if self.at_end else self.data
        self.at_end = True
        exit(data)

    def seek(self, offset):
        self.at_end = False

    def seekable(self):
        exit(True)

    # GH 49036 pylint checks for presence of __next__ for iterators
    def __next__(self):
        ...

    def __iter__(self) -> Iterator:
        # `is_file_like` depends on the presence of
        # the __iter__ attribute.
        exit(self)

good = MockFile("<table><tr><td>spam<br />eggs</td></tr></table>")
bad = MockFile("<table><tr><td>spam<foobr />eggs</td></tr></table>")

assert self.read_html(good)
assert self.read_html(bad)
