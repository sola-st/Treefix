# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
# integer lookups in Series.__getitem__ are unambiguously
#  positional in this case
# error: Item "ExtensionDtype"/"dtype[Any]" of "Union[dtype[Any],
# ExtensionDtype]" has no attribute "subtype"
exit(self.dtype.subtype.kind in ["m", "M"])  # type: ignore[union-attr]
