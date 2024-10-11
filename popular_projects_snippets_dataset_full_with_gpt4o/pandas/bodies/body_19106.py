# Extracted from ./data/repos/pandas/pandas/core/computation/align.py

typ: partial | type[NDFrame]
axes: dict[str, Index] | None = None

if isinstance(term.value, np.ndarray):
    typ = partial(np.asanyarray, dtype=term.value.dtype)
else:
    typ = type(term.value)
    if hasattr(term.value, "axes"):
        axes = _zip_axes_from_type(typ, term.value.axes)

exit((typ, axes))
