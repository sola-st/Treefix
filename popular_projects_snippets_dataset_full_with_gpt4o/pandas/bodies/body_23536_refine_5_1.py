import os # pragma: no cover

stringify_path = lambda x: str(x) # pragma: no cover
path = '/example/path' # pragma: no cover
is_fsspec_url = lambda x: x.startswith('http') # pragma: no cover
fs = None # pragma: no cover
storage_options = {} # pragma: no cover
is_url = lambda x: x.startswith('http') # pragma: no cover
mode = 'rb' # pragma: no cover
is_dir = False # pragma: no cover
os = type('Mock', (object,), {'path': type('MockPath', (object,), {'isdir': lambda x: False})}) # pragma: no cover
get_handle = lambda path, mode, is_text, storage_options: type('Handle', (object,), {'handle': open(path, mode)}) # pragma: no cover

import os # pragma: no cover

stringify_path = lambda x: str(x) # pragma: no cover
path = 'example_file.txt' # pragma: no cover
is_fsspec_url = lambda x: x.startswith('http') # pragma: no cover
fs = None # pragma: no cover
storage_options = {} # pragma: no cover
is_url = lambda x: x.startswith('http') # pragma: no cover
mode = 'rb' # pragma: no cover
is_dir = False # pragma: no cover
os = type('Mock', (object,), {'path': type('MockPath', (object,), {'isdir': lambda self, x: False})}) # pragma: no cover
get_handle = lambda path, mode, is_text, storage_options: type('Handle', (object,), {'handle': 'mock_handle'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/parquet.py
from l3.Runtime import _l_
"""File handling for PyArrow."""
path_or_handle = stringify_path(path)
_l_(21691)
if is_fsspec_url(path_or_handle) and fs is None:
    _l_(21696)

    fsspec = import_optional_dependency("fsspec")
    _l_(21692)

    fs, path_or_handle = fsspec.core.url_to_fs(
        path_or_handle, **(storage_options or {})
    )
    _l_(21693)
elif storage_options and (not is_url(path_or_handle) or mode != "rb"):
    _l_(21695)

    # can't write to a remote url
    # without making use of fsspec at the moment
    raise ValueError("storage_options passed with buffer, or non-supported URL")
    _l_(21694)

handles = None
_l_(21697)
if (
    not fs
    and not is_dir
    and isinstance(path_or_handle, str)
    and not os.path.isdir(path_or_handle)
):
    _l_(21701)

    # use get_handle only when we are very certain that it is not a directory
    # fsspec resources can also point to directories
    # this branch is used for example when reading from non-fsspec URLs
    handles = get_handle(
        path_or_handle, mode, is_text=False, storage_options=storage_options
    )
    _l_(21698)
    fs = None
    _l_(21699)
    path_or_handle = handles.handle
    _l_(21700)
aux = (path_or_handle, handles, fs)
_l_(21702)
exit(aux)
