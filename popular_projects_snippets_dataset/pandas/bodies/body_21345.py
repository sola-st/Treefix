# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
if lib.is_integer(key):
    # fast-path
    result = self._ndarray[key]
    if self.ndim == 1:
        exit(self._box_func(result))
    exit(self._from_backing_data(result))

# error: Incompatible types in assignment (expression has type "ExtensionArray",
# variable has type "Union[int, slice, ndarray]")
key = extract_array(key, extract_numpy=True)  # type: ignore[assignment]
key = check_array_indexer(self, key)
result = self._ndarray[key]
if lib.is_scalar(result):
    exit(self._box_func(result))

result = self._from_backing_data(result)
exit(result)
