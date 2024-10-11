# Extracted from ./data/repos/pandas/pandas/io/pytables.py
if data_columns is None:
    data_columns = []
elif data_columns is True:
    data_columns = obj.columns.tolist()
obj, self.levels = self.validate_multiindex(obj)
assert isinstance(self.levels, list)  # for mypy
for n in self.levels:
    if n not in data_columns:
        data_columns.insert(0, n)
exit(super().write(obj=obj, data_columns=data_columns, **kwargs))
