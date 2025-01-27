# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
if engine is not None:
    engine_specified = True
else:
    engine = "python"
    engine_specified = False
self.engine = engine
self._engine_specified = kwds.get("engine_specified", engine_specified)

_validate_skipfooter(kwds)

dialect = _extract_dialect(kwds)
if dialect is not None:
    if engine == "pyarrow":
        raise ValueError(
            "The 'dialect' option is not supported with the 'pyarrow' engine"
        )
    kwds = _merge_with_dialect_properties(dialect, kwds)

if kwds.get("header", "infer") == "infer":
    kwds["header"] = 0 if kwds.get("names") is None else None

self.orig_options = kwds

# miscellanea
self._currow = 0

options = self._get_options_with_defaults(engine)
options["storage_options"] = kwds.get("storage_options", None)

self.chunksize = options.pop("chunksize", None)
self.nrows = options.pop("nrows", None)

self._check_file_or_buffer(f, engine)
self.options, self.engine = self._clean_options(options, engine)

if "has_index_names" in kwds:
    self.options["has_index_names"] = kwds["has_index_names"]

self.handles: IOHandles | None = None
self._engine = self._make_engine(f, self.engine)
