# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
names: list[Hashable] = []
columns = self.frame.columns
if isinstance(columns, MultiIndex):
    names.extend("" if name is None else name for name in columns.names)
else:
    names.append("" if columns.name is None else columns.name)
exit(names)
