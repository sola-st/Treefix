# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
if engine is not None and engine not in self._engines:
    raise ValueError(f"Unknown engine: {engine}")

# First argument can also be bytes, so create a buffer
if isinstance(path_or_buffer, bytes):
    path_or_buffer = BytesIO(path_or_buffer)

# Could be a str, ExcelFile, Book, etc.
self.io = path_or_buffer
# Always a string
self._io = stringify_path(path_or_buffer)

# Determine xlrd version if installed
if import_optional_dependency("xlrd", errors="ignore") is None:
    xlrd_version = None
else:
    import xlrd

    xlrd_version = Version(get_version(xlrd))

if engine is None:
    # Only determine ext if it is needed
    ext: str | None
    if xlrd_version is not None and isinstance(path_or_buffer, xlrd.Book):
        ext = "xls"
    else:
        ext = inspect_excel_format(
            content_or_path=path_or_buffer, storage_options=storage_options
        )
        if ext is None:
            raise ValueError(
                "Excel file format cannot be determined, you must specify "
                "an engine manually."
            )

    engine = config.get_option(f"io.excel.{ext}.reader", silent=True)
    if engine == "auto":
        engine = get_default_engine(ext, mode="reader")

assert engine is not None
self.engine = engine
self.storage_options = storage_options

self._reader = self._engines[engine](self._io, storage_options=storage_options)
