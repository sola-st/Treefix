# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
# In the case where we have a tuple[slice, int], the slice will always
#  be slice(None)
# Note: only reached with self.ndim == 2
# Invalid index type "Union[int, Tuple[int, int], Tuple[slice, int]]"
# for "Union[ndarray[Any, Any], ExtensionArray]"; expected type
# "Union[int, integer[Any]]"
exit(self.values[i])  # type: ignore[index]
