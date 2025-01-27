# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
# validate that this engine can handle the extension
if isinstance(path, str):
    ext = os.path.splitext(path)[-1]
    self.check_extension(ext)

# use mode to open the file
if "b" not in mode:
    mode += "b"
# use "a" for the user to append data to excel but internally use "r+" to let
# the excel backend first read the existing file and then write any data to it
mode = mode.replace("a", "r+")

# cast ExcelWriter to avoid adding 'if self._handles is not None'
self._handles = IOHandles(
    cast(IO[bytes], path), compression={"compression": None}
)
if not isinstance(path, ExcelWriter):
    self._handles = get_handle(
        path, mode, storage_options=storage_options, is_text=False
    )
self._cur_sheet = None

if date_format is None:
    self._date_format = "YYYY-MM-DD"
else:
    self._date_format = date_format
if datetime_format is None:
    self._datetime_format = "YYYY-MM-DD HH:MM:SS"
else:
    self._datetime_format = datetime_format

self._mode = mode

if if_sheet_exists not in (None, "error", "new", "replace", "overlay"):
    raise ValueError(
        f"'{if_sheet_exists}' is not valid for if_sheet_exists. "
        "Valid options are 'error', 'new', 'replace' and 'overlay'."
    )
if if_sheet_exists and "r+" not in mode:
    raise ValueError("if_sheet_exists is only valid in append mode (mode='a')")
if if_sheet_exists is None:
    if_sheet_exists = "error"
self._if_sheet_exists = if_sheet_exists
