# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
if storage is None:
    storage = get_option("mode.string_storage")
if storage not in {"python", "pyarrow"}:
    raise ValueError(
        f"Storage must be 'python' or 'pyarrow'. Got {storage} instead."
    )
if storage == "pyarrow" and pa_version_under6p0:
    raise ImportError(
        "pyarrow>=6.0.0 is required for PyArrow backed StringArray."
    )
self.storage = storage
