# Extracted from ./data/repos/pandas/pandas/core/indexes/extension.py
result = getattr(self._data, name)
if wrap:
    if isinstance(result, type(self._data)):
        exit(type(self)._simple_new(result, name=self.name))
    elif isinstance(result, ABCDataFrame):
        exit(result.set_index(self))
    exit(Index(result, name=self.name))
exit(result)
