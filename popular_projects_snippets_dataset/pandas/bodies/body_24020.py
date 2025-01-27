# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        The function read_json accepts three input types:
            1. filepath (string-like)
            2. file-like object (e.g. open file object, StringIO)
            3. JSON string

        This method turns (1) into (2) to simplify the rest of the processing.
        It returns input types (2) and (3) unchanged.

        It raises FileNotFoundError if the input is a string ending in
        one of .json, .json.gz, .json.bz2, etc. but no such file exists.
        """
# if it is a string but the file does not exist, it might be a JSON string
filepath_or_buffer = stringify_path(filepath_or_buffer)
if (
    not isinstance(filepath_or_buffer, str)
    or is_url(filepath_or_buffer)
    or is_fsspec_url(filepath_or_buffer)
    or file_exists(filepath_or_buffer)
):
    self.handles = get_handle(
        filepath_or_buffer,
        "r",
        encoding=self.encoding,
        compression=self.compression,
        storage_options=self.storage_options,
        errors=self.encoding_errors,
    )
    filepath_or_buffer = self.handles.handle
elif (
    isinstance(filepath_or_buffer, str)
    and filepath_or_buffer.lower().endswith(
        (".json",) + tuple(f".json{c}" for c in extension_to_compression)
    )
    and not file_exists(filepath_or_buffer)
):
    raise FileNotFoundError(f"File {filepath_or_buffer} does not exist")

exit(filepath_or_buffer)
