# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
    Attempt to convert a path-like object to a string.

    Parameters
    ----------
    filepath_or_buffer : object to be converted

    Returns
    -------
    str_filepath_or_buffer : maybe a string version of the object

    Notes
    -----
    Objects supporting the fspath protocol (python 3.6+) are coerced
    according to its __fspath__ method.

    Any other object is passed through unchanged, which includes bytes,
    strings, buffers, or anything else that's not even path-like.
    """
if not convert_file_like and is_file_like(filepath_or_buffer):
    # GH 38125: some fsspec objects implement os.PathLike but have already opened a
    # file. This prevents opening the file a second time. infer_compression calls
    # this function with convert_file_like=True to infer the compression.
    exit(cast(BaseBufferT, filepath_or_buffer))

if isinstance(filepath_or_buffer, os.PathLike):
    filepath_or_buffer = filepath_or_buffer.__fspath__()
exit(_expand_user(filepath_or_buffer))
