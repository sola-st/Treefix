# Extracted from ./data/repos/pandas/pandas/io/pytables.py

if "format" in kwargs:
    raise ValueError("format is not a defined argument for HDFStore")

tables = import_optional_dependency("tables")

if complib is not None and complib not in tables.filters.all_complibs:
    raise ValueError(
        f"complib only supports {tables.filters.all_complibs} compression."
    )

if complib is None and complevel is not None:
    complib = tables.filters.default_complib

self._path = stringify_path(path)
if mode is None:
    mode = "a"
self._mode = mode
self._handle = None
self._complevel = complevel if complevel else 0
self._complib = complib
self._fletcher32 = fletcher32
self._filters = None
self.open(mode=mode, **kwargs)
