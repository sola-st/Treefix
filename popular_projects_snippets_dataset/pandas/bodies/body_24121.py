# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
# First argument can also be bytes, so create a buffer
if isinstance(filepath_or_buffer, bytes):
    filepath_or_buffer = BytesIO(filepath_or_buffer)

self.handles = IOHandles(
    handle=filepath_or_buffer, compression={"method": None}
)
if not isinstance(filepath_or_buffer, (ExcelFile, self._workbook_class)):
    self.handles = get_handle(
        filepath_or_buffer, "rb", storage_options=storage_options, is_text=False
    )

if isinstance(self.handles.handle, self._workbook_class):
    self.book = self.handles.handle
elif hasattr(self.handles.handle, "read"):
    # N.B. xlrd.Book has a read attribute too
    self.handles.handle.seek(0)
    try:
        self.book = self.load_workbook(self.handles.handle)
    except Exception:
        self.close()
        raise
else:
    raise ValueError(
        "Must explicitly set engine if not passing in buffer or path for io."
    )
