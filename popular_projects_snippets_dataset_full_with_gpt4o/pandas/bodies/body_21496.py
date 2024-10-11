# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/dtype.py
super().__init__("pyarrow")
if pa_version_under6p0:
    raise ImportError("pyarrow>=6.0.0 is required for ArrowDtype")
if not isinstance(pyarrow_dtype, pa.DataType):
    raise ValueError(
        f"pyarrow_dtype ({pyarrow_dtype}) must be an instance "
        f"of a pyarrow.DataType. Got {type(pyarrow_dtype)} instead."
    )
self.pyarrow_dtype = pyarrow_dtype
