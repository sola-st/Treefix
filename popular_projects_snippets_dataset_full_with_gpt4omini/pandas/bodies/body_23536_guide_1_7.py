import os # pragma: no cover
from urllib.parse import urlparse # pragma: no cover

path = 'example.txt' # pragma: no cover
storage_options = None # pragma: no cover
mode = 'rb' # pragma: no cover
is_dir = False # pragma: no cover
fs = None # pragma: no cover
path_or_handle = 'example.txt' # pragma: no cover
def is_fsspec_url(url): return False # pragma: no cover
def is_url(url): return not url.startswith('s3://') # pragma: no cover
handles = type('MockHandle', (object,), {'handle': open(path_or_handle, mode)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/parquet.py
from l3.Runtime import _l_
"""File handling for PyArrow."""
path_or_handle = stringify_path(path)
_l_(10400)
if is_fsspec_url(path_or_handle) and fs is None:
    _l_(10405)

    fsspec = import_optional_dependency("fsspec")
    _l_(10401)

    fs, path_or_handle = fsspec.core.url_to_fs(
        path_or_handle, **(storage_options or {})
    )
    _l_(10402)
elif storage_options and (not is_url(path_or_handle) or mode != "rb"):
    _l_(10404)

    # can't write to a remote url
    # without making use of fsspec at the moment
    raise ValueError("storage_options passed with buffer, or non-supported URL")
    _l_(10403)

handles = None
_l_(10406)
if (
    not fs
    and not is_dir
    and isinstance(path_or_handle, str)
    and not os.path.isdir(path_or_handle)
):
    _l_(10410)

    # use get_handle only when we are very certain that it is not a directory
    # fsspec resources can also point to directories
    # this branch is used for example when reading from non-fsspec URLs
    handles = get_handle(
        path_or_handle, mode, is_text=False, storage_options=storage_options
    )
    _l_(10407)
    fs = None
    _l_(10408)
    path_or_handle = handles.handle
    _l_(10409)
aux = (path_or_handle, handles, fs)
_l_(10411)
exit(aux)
