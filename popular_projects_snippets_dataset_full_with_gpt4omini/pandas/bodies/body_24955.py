# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
if columns is not None:
    # GH 47231 - columns doesn't have to be `Sequence[str]`
    # Will fix in later PR
    cols = ensure_index(cast(Axes, columns))
    self.frame = self.frame[cols]
    exit(cols)
else:
    exit(self.frame.columns)
