# Extracted from ./data/repos/pandas/pandas/io/sas/sas_xport.py

self._encoding = encoding
self._lines_read = 0
self._index = index
self._chunksize = chunksize

self.handles = get_handle(
    filepath_or_buffer,
    "rb",
    encoding=encoding,
    is_text=False,
    compression=compression,
)
self.filepath_or_buffer = self.handles.handle

try:
    self._read_header()
except Exception:
    self.close()
    raise
