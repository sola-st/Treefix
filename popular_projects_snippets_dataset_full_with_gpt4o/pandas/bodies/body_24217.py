# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py

self.index = index
self.convert_dates = convert_dates
self.blank_missing = blank_missing
self.chunksize = chunksize
self.encoding = encoding
self.convert_text = convert_text
self.convert_header_text = convert_header_text

self.default_encoding = "latin-1"
self.compression = b""
self.column_names_raw: list[bytes] = []
self.column_names: list[str | bytes] = []
self.column_formats: list[str | bytes] = []
self.columns: list[_Column] = []

self._current_page_data_subheader_pointers: list[tuple[int, int]] = []
self._cached_page = None
self._column_data_lengths: list[int] = []
self._column_data_offsets: list[int] = []
self._column_types: list[bytes] = []

self._current_row_in_file_index = 0
self._current_row_on_page_index = 0
self._current_row_in_file_index = 0

self.handles = get_handle(
    path_or_buf, "rb", is_text=False, compression=compression
)

self._path_or_buf = self.handles.handle

# Same order as const.SASIndex
self._subheader_processors = [
    self._process_rowsize_subheader,
    self._process_columnsize_subheader,
    self._process_subheader_counts,
    self._process_columntext_subheader,
    self._process_columnname_subheader,
    self._process_columnattributes_subheader,
    self._process_format_subheader,
    self._process_columnlist_subheader,
    None,  # Data
]

try:
    self._get_properties()
    self._parse_metadata()
except Exception:
    self.close()
    raise
