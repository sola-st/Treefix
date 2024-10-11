# Extracted from ./data/repos/pandas/pandas/core/arrays/numeric.py
dtype_cls = cls._dtype_cls
default_dtype = dtype_cls._default_np_dtype
mask = None
values, mask, _, _ = _coerce_to_data_and_mask(
    value, mask, dtype, copy, dtype_cls, default_dtype
)
exit((values, mask))
