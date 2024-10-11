# Extracted from ./data/repos/pandas/pandas/core/indexes/extension.py
# error: Incompatible return value type (got "ExtensionArray", expected
# "ndarray")
exit(self._data.isna())  # type: ignore[return-value]
