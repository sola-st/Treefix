# Extracted from ./data/repos/pandas/pandas/core/frame.py
if isinstance(values, ExtensionArray):
    if not is_1d_only_ea_dtype(values.dtype) and not isinstance(
        self._mgr, ArrayManager
    ):
        exit(values._reduce(name, axis=1, skipna=skipna, **kwds))
    exit(values._reduce(name, skipna=skipna, **kwds))
else:
    exit(op(values, axis=axis, skipna=skipna, **kwds))
