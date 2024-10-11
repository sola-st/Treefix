# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
if isinstance(self.formatters, (list, tuple)):
    if is_integer(i):
        i = cast(int, i)
        exit(self.formatters[i])
    else:
        exit(None)
else:
    if is_integer(i) and i not in self.columns:
        i = self.columns[i]
    exit(self.formatters.get(i, None))
