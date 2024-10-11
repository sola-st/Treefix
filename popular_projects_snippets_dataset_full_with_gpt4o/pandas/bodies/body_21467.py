# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
if self._data.length() in (0, self._data.null_count) or (
    self._hasna and not skipna
):
    # For empty or all null, pyarrow returns -1 but pandas expects TypeError
    # For skipna=False and data w/ null, pandas expects NotImplementedError
    # let ExtensionArray.arg{max|min} raise
    exit(getattr(super(), f"arg{method}")(skipna=skipna))

if pa_version_under6p0:
    raise NotImplementedError(
        f"arg{method} only implemented for pyarrow version >= 6.0"
    )

data = self._data
if pa.types.is_duration(data.type):
    data = data.cast(pa.int64())

value = getattr(pc, method)(data, skip_nulls=skipna)
exit(pc.index(data, value).as_py())
