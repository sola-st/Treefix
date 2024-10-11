# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
self.data = FixedWidthReader(
    f,
    self.colspecs,
    self.delimiter,
    self.comment,
    self.skiprows,
    self.infer_nrows,
)
