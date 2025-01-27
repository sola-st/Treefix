# Extracted from ./data/repos/pandas/pandas/io/json/_json.py

self.orient = orient
self.typ = typ
self.dtype = dtype
self.convert_axes = convert_axes
self.convert_dates = convert_dates
self.keep_default_dates = keep_default_dates
self.precise_float = precise_float
self.date_unit = date_unit
self.encoding = encoding
self.compression = compression
self.storage_options = storage_options
self.lines = lines
self.chunksize = chunksize
self.nrows_seen = 0
self.nrows = nrows
self.encoding_errors = encoding_errors
self.handles: IOHandles[str] | None = None
self.use_nullable_dtypes = use_nullable_dtypes

if self.chunksize is not None:
    self.chunksize = validate_integer("chunksize", self.chunksize, 1)
    if not self.lines:
        raise ValueError("chunksize can only be passed if lines=True")
if self.nrows is not None:
    self.nrows = validate_integer("nrows", self.nrows, 0)
    if not self.lines:
        raise ValueError("nrows can only be passed if lines=True")

data = self._get_data_from_filepath(filepath_or_buffer)
self.data = self._preprocess_data(data)
