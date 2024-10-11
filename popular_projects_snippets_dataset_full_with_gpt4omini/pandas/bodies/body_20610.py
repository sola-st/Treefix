# Extracted from ./data/repos/pandas/pandas/core/indexes/extension.py
if "inplace" in kwargs:
    raise ValueError(f"cannot use inplace with {type(self).__name__}")
result = attr(self._data, *args, **kwargs)
if wrap:
    if isinstance(result, type(self._data)):
        exit(type(self)._simple_new(result, name=self.name))
    elif isinstance(result, ABCDataFrame):
        exit(result.set_index(self))
    exit(Index(result, name=self.name))
exit(result)
