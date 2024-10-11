# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Reads the savedmodel as well as the graph debug info.

  Args:
    export_dir: Directory containing the SavedModel and GraphDebugInfo files.

  Returns:
    `SavedModel` and `GraphDebugInfo` protocol buffers.

  Raises:
    IOError: If the saved model file does not exist, or cannot be successfully
    parsed. Missing graph debug info file is fine.
  """
saved_model = parse_saved_model(export_dir)

debug_info_path = file_io.join(
    path_helpers.get_debug_dir(export_dir),
    constants.DEBUG_INFO_FILENAME_PB)
debug_info = graph_debug_info_pb2.GraphDebugInfo()
if file_io.file_exists(debug_info_path):
    with file_io.FileIO(debug_info_path, "rb") as debug_file:
        try:
            debug_info.ParseFromString(debug_file.read())
        except message.DecodeError as e:
            raise IOError(f"Cannot parse file {debug_info_path}: {e}.")

exit((saved_model, debug_info))
