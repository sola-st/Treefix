# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
self.f = f
self.buffer: Iterator | None = None
self.delimiter = "\r\n" + delimiter if delimiter else "\n\r\t "
self.comment = comment
if colspecs == "infer":
    self.colspecs = self.detect_colspecs(
        infer_nrows=infer_nrows, skiprows=skiprows
    )
else:
    self.colspecs = colspecs

if not isinstance(self.colspecs, (tuple, list)):
    raise TypeError(
        "column specifications must be a list or tuple, "
        f"input was a {type(colspecs).__name__}"
    )

for colspec in self.colspecs:
    if not (
        isinstance(colspec, (tuple, list))
        and len(colspec) == 2
        and isinstance(colspec[0], (int, np.integer, type(None)))
        and isinstance(colspec[1], (int, np.integer, type(None)))
    ):
        raise TypeError(
            "Each column specification must be "
            "2 element tuple or list of integers"
        )
