# Extracted from ./data/repos/pandas/pandas/core/indexes/numeric.py
# error: Invalid index type "Union[dtype[Any], ExtensionDtype]" for
# "Dict[dtype[Any], Type[IndexEngine]]"; expected type "dtype[Any]"
exit(self._engine_types[self.dtype])  # type: ignore[index]
