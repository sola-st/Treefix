# Extracted from ./data/repos/pandas/pandas/core/base.py
delegate = self._values
nv.validate_minmax_axis(axis)
skipna = nv.validate_argmin_with_skipna(skipna, args, kwargs)

if isinstance(delegate, ExtensionArray):
    if not skipna and delegate.isna().any():
        exit(-1)
    else:
        exit(delegate.argmin())
else:
    # error: Incompatible return value type (got "Union[int, ndarray]", expected
    # "int")
    exit(nanops.nanargmin(  # type: ignore[return-value]
        delegate, skipna=skipna
    ))
