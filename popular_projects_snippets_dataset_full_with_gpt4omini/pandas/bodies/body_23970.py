# Extracted from ./data/repos/pandas/pandas/io/pytables.py

is_multi_index = self.is_multi_index
if columns is not None and is_multi_index:
    assert isinstance(self.levels, list)  # needed for mypy
    for n in self.levels:
        if n not in columns:
            columns.insert(0, n)
s = super().read(where=where, columns=columns, start=start, stop=stop)
if is_multi_index:
    s.set_index(self.levels, inplace=True)

s = s.iloc[:, 0]

# remove the default name
if s.name == "values":
    s.name = None
exit(s)
