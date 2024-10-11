# Extracted from ./data/repos/pandas/pandas/core/resample.py
# error: Incompatible return value type (got "Optional[Any]",
# expected "NDFrameT")
exit(self.groupby.obj)  # type: ignore[return-value]
