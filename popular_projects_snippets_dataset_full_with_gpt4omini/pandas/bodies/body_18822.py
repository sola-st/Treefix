# Extracted from ./data/repos/pandas/pandas/_testing/_io.py
"""
    Write data to a compressed file.

    Parameters
    ----------
    compression : {'gzip', 'bz2', 'zip', 'xz', 'zstd'}
        The compression type to use.
    path : str
        The file path to write the data.
    data : str
        The data to write.
    dest : str, default "test"
        The destination file (for ZIP only)

    Raises
    ------
    ValueError : An invalid compression value was passed in.
    """
args: tuple[Any, ...] = (data,)
mode = "wb"
method = "write"
compress_method: Callable

if compression == "zip":
    compress_method = zipfile.ZipFile
    mode = "w"
    args = (dest, data)
    method = "writestr"
elif compression == "tar":
    compress_method = tarfile.TarFile
    mode = "w"
    file = tarfile.TarInfo(name=dest)
    bytes = io.BytesIO(data)
    file.size = len(data)
    args = (file, bytes)
    method = "addfile"
elif compression == "gzip":
    compress_method = gzip.GzipFile
elif compression == "bz2":
    compress_method = bz2.BZ2File
elif compression == "zstd":
    compress_method = import_optional_dependency("zstandard").open
elif compression == "xz":
    compress_method = get_lzma_file()
else:
    raise ValueError(f"Unrecognized compression type: {compression}")

with compress_method(path, mode=mode) as f:
    getattr(f, method)(*args)
