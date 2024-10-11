# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
    If the filepath_or_buffer is a url, translate and return the buffer.
    Otherwise passthrough.

    Parameters
    ----------
    filepath_or_buffer : a url, filepath (str, py.path.local or pathlib.Path),
                         or buffer
    {compression_options}

        .. versionchanged:: 1.4.0 Zstandard support.

    encoding : the encoding to use to decode bytes, default is 'utf-8'
    mode : str, optional

    {storage_options}

        .. versionadded:: 1.2.0

    ..versionchange:: 1.2.0

      Returns the dataclass IOArgs.
    """
filepath_or_buffer = stringify_path(filepath_or_buffer)

# handle compression dict
compression_method, compression = get_compression_method(compression)
compression_method = infer_compression(filepath_or_buffer, compression_method)

# GH21227 internal compression is not used for non-binary handles.
if compression_method and hasattr(filepath_or_buffer, "write") and "b" not in mode:
    warnings.warn(
        "compression has no effect when passing a non-binary object as input.",
        RuntimeWarning,
        stacklevel=find_stack_level(),
    )
    compression_method = None

compression = dict(compression, method=compression_method)

# bz2 and xz do not write the byte order mark for utf-16 and utf-32
# print a warning when writing such files
if (
    "w" in mode
    and compression_method in ["bz2", "xz"]
    and encoding in ["utf-16", "utf-32"]
):
    warnings.warn(
        f"{compression} will not write the byte order mark for {encoding}",
        UnicodeWarning,
        stacklevel=find_stack_level(),
    )

# Use binary mode when converting path-like objects to file-like objects (fsspec)
# except when text mode is explicitly requested. The original mode is returned if
# fsspec is not used.
fsspec_mode = mode
if "t" not in fsspec_mode and "b" not in fsspec_mode:
    fsspec_mode += "b"

if isinstance(filepath_or_buffer, str) and is_url(filepath_or_buffer):
    # TODO: fsspec can also handle HTTP via requests, but leaving this
    # unchanged. using fsspec appears to break the ability to infer if the
    # server responded with gzipped data
    storage_options = storage_options or {}

    # waiting until now for importing to match intended lazy logic of
    # urlopen function defined elsewhere in this module
    import urllib.request

    # assuming storage_options is to be interpreted as headers
    req_info = urllib.request.Request(filepath_or_buffer, headers=storage_options)
    with urlopen(req_info) as req:
        content_encoding = req.headers.get("Content-Encoding", None)
        if content_encoding == "gzip":
            # Override compression based on Content-Encoding header
            compression = {"method": "gzip"}
        reader = BytesIO(req.read())
    exit(IOArgs(
        filepath_or_buffer=reader,
        encoding=encoding,
        compression=compression,
        should_close=True,
        mode=fsspec_mode,
    ))

if is_fsspec_url(filepath_or_buffer):
    assert isinstance(
        filepath_or_buffer, str
    )  # just to appease mypy for this branch
    # two special-case s3-like protocols; these have special meaning in Hadoop,
    # but are equivalent to just "s3" from fsspec's point of view
    # cc #11071
    if filepath_or_buffer.startswith("s3a://"):
        filepath_or_buffer = filepath_or_buffer.replace("s3a://", "s3://")
    if filepath_or_buffer.startswith("s3n://"):
        filepath_or_buffer = filepath_or_buffer.replace("s3n://", "s3://")
    fsspec = import_optional_dependency("fsspec")

    # If botocore is installed we fallback to reading with anon=True
    # to allow reads from public buckets
    err_types_to_retry_with_anon: list[Any] = []
    try:
        import_optional_dependency("botocore")
        from botocore.exceptions import (
            ClientError,
            NoCredentialsError,
        )

        err_types_to_retry_with_anon = [
            ClientError,
            NoCredentialsError,
            PermissionError,
        ]
    except ImportError:
        pass

    try:
        file_obj = fsspec.open(
            filepath_or_buffer, mode=fsspec_mode, **(storage_options or {})
        ).open()
    # GH 34626 Reads from Public Buckets without Credentials needs anon=True
    except tuple(err_types_to_retry_with_anon):
        if storage_options is None:
            storage_options = {"anon": True}
        else:
            # don't mutate user input.
            storage_options = dict(storage_options)
            storage_options["anon"] = True
        file_obj = fsspec.open(
            filepath_or_buffer, mode=fsspec_mode, **(storage_options or {})
        ).open()

    exit(IOArgs(
        filepath_or_buffer=file_obj,
        encoding=encoding,
        compression=compression,
        should_close=True,
        mode=fsspec_mode,
    ))
elif storage_options:
    raise ValueError(
        "storage_options passed with file object or non-fsspec file path"
    )

if isinstance(filepath_or_buffer, (str, bytes, mmap.mmap)):
    exit(IOArgs(
        filepath_or_buffer=_expand_user(filepath_or_buffer),
        encoding=encoding,
        compression=compression,
        should_close=False,
        mode=mode,
    ))

# is_file_like requires (read | write) & __iter__ but __iter__ is only
# needed for read_csv(engine=python)
if not (
    hasattr(filepath_or_buffer, "read") or hasattr(filepath_or_buffer, "write")
):
    msg = f"Invalid file path or buffer object type: {type(filepath_or_buffer)}"
    raise ValueError(msg)

exit(IOArgs(
    filepath_or_buffer=filepath_or_buffer,
    encoding=encoding,
    compression=compression,
    should_close=False,
    mode=mode,
))
