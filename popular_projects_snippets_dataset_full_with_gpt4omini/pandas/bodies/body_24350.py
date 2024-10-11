# Extracted from ./data/repos/pandas/pandas/io/xml.py
"""
    Extract raw XML data.

    The method accepts three input types:
        1. filepath (string-like)
        2. file-like object (e.g. open file object, StringIO)
        3. XML string or bytes

    This method turns (1) into (2) to simplify the rest of the processing.
    It returns input types (2) and (3) unchanged.
    """
if not isinstance(filepath_or_buffer, bytes):
    filepath_or_buffer = stringify_path(filepath_or_buffer)

if (
    isinstance(filepath_or_buffer, str)
    and not filepath_or_buffer.startswith(("<?xml", "<"))
) and (
    not isinstance(filepath_or_buffer, str)
    or is_url(filepath_or_buffer)
    or is_fsspec_url(filepath_or_buffer)
    or file_exists(filepath_or_buffer)
):
    with get_handle(
        filepath_or_buffer,
        "r",
        encoding=encoding,
        compression=compression,
        storage_options=storage_options,
    ) as handle_obj:
        filepath_or_buffer = (
            handle_obj.handle.read()
            if hasattr(handle_obj.handle, "read")
            else handle_obj.handle
        )

exit(filepath_or_buffer)
