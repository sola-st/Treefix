# Extracted from ./data/repos/pandas/pandas/io/stata.py
super().__init__()
self.col_sizes: list[int] = []

# Arguments to the reader (can be temporarily overridden in
# calls to read).
self._convert_dates = convert_dates
self._convert_categoricals = convert_categoricals
self._index_col = index_col
self._convert_missing = convert_missing
self._preserve_dtypes = preserve_dtypes
self._columns = columns
self._order_categoricals = order_categoricals
self._encoding = ""
self._chunksize = chunksize
self._using_iterator = False
if self._chunksize is None:
    self._chunksize = 1
elif not isinstance(chunksize, int) or chunksize <= 0:
    raise ValueError("chunksize must be a positive integer when set.")

# State variables for the file
self._has_string_data = False
self._missing_values = False
self._can_read_value_labels = False
self._column_selector_set = False
self._value_labels_read = False
self._data_read = False
self._dtype: np.dtype | None = None
self._lines_read = 0

self._native_byteorder = _set_endianness(sys.byteorder)
with get_handle(
    path_or_buf,
    "rb",
    storage_options=storage_options,
    is_text=False,
    compression=compression,
) as handles:
    # Copy to BytesIO, and ensure no encoding
    self.path_or_buf = BytesIO(handles.handle.read())

self._read_header()
self._setup_dtype()
