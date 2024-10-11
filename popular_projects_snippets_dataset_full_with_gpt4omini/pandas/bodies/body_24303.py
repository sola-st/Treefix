# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
    Get the compression method for filepath_or_buffer. If compression='infer',
    the inferred compression method is returned. Otherwise, the input
    compression method is returned unchanged, unless it's invalid, in which
    case an error is raised.

    Parameters
    ----------
    filepath_or_buffer : str or file handle
        File path or object.
    {compression_options}

        .. versionchanged:: 1.4.0 Zstandard support.

    Returns
    -------
    string or None

    Raises
    ------
    ValueError on invalid compression specified.
    """
if compression is None:
    exit(None)

# Infer compression
if compression == "infer":
    # Convert all path types (e.g. pathlib.Path) to strings
    filepath_or_buffer = stringify_path(filepath_or_buffer, convert_file_like=True)
    if not isinstance(filepath_or_buffer, str):
        # Cannot infer compression of a buffer, assume no compression
        exit(None)

    # Infer compression from the filename/URL extension
    for extension, compression in extension_to_compression.items():
        if filepath_or_buffer.lower().endswith(extension):
            exit(compression)
    exit(None)

# Compression has been specified. Check that it's valid
if compression in _supported_compressions:
    exit(compression)

valid = ["infer", None] + sorted(_supported_compressions)
msg = (
    f"Unrecognized compression type: {compression}\n"
    f"Valid compression types are {valid}"
)
raise ValueError(msg)
