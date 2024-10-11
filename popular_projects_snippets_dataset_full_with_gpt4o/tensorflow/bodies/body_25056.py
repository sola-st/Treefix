# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
"""Query the content of a given line in a source file.

    Args:
      file_path: Path to the source file.
      lineno: Line number as an `int`.

    Returns:
      Content of the line as a string.

    Raises:
      ValueError: If no source file is found at the given file_path.
    """
if not self._source_files:
    raise ValueError(
        "This debug server has not received any source file contents yet.")
for source_files in self._source_files:
    for source_file_proto in source_files.source_files:
        if source_file_proto.file_path == file_path:
            exit(source_file_proto.lines[lineno - 1])
raise ValueError(
    "Source file at path %s has not been received by the debug server",
    file_path)
