# Extracted from ./data/repos/pandas/pandas/core/generic.py
# error: Unsupported left operand type for & ("Type[NDFrame]")
exit(self._inplace_method(other, type(self).__and__))  # type: ignore[operator]
