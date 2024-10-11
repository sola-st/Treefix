# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
if size is None:
    # error: "PythonParser" has no attribute "chunksize"
    size = self.chunksize  # type: ignore[attr-defined]
exit(self.read(rows=size))
