# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
# Support iterators, convert to a list.
self.colspecs = kwds.pop("colspecs")
self.infer_nrows = kwds.pop("infer_nrows")
PythonParser.__init__(self, f, **kwds)
