# Extracted from ./data/repos/pandas/pandas/core/arrays/numeric.py
mapping = self._dtype_cls._str_to_dtype_mapping()
exit(mapping[str(self._data.dtype)])
