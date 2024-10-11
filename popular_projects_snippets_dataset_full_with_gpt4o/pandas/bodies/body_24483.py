# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
# Argument 1 to "next" has incompatible type "Union[IO[str],
# ReadCsvBuffer[str]]"; expected "SupportsNext[str]"
if self.buffer is not None:
    try:
        line = next(self.buffer)
    except StopIteration:
        self.buffer = None
        line = next(self.f)  # type: ignore[arg-type]
else:
    line = next(self.f)  # type: ignore[arg-type]
# Note: 'colspecs' is a sequence of half-open intervals.
exit([line[from_:to].strip(self.delimiter) for (from_, to) in self.colspecs])
