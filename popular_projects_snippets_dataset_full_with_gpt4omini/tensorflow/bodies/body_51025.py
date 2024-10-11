# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Reads the savedmodel.pb or savedmodel.pbtxt file containing `SavedModel`.

  Args:
    export_dir: String or Pathlike, path to the directory containing the
    SavedModel file.

  Returns:
    A `SavedModel` protocol buffer.

  Raises:
    IOError: If the file does not exist, or cannot be successfully parsed.
  """
# Build the path to the SavedModel in pbtxt format.
path_to_pbtxt = file_io.join(
    compat.as_bytes(compat.path_to_str(export_dir)),
    compat.as_bytes(constants.SAVED_MODEL_FILENAME_PBTXT))
# Build the path to the SavedModel in pb format.
path_to_pb = file_io.join(
    compat.as_bytes(compat.path_to_str(export_dir)),
    compat.as_bytes(constants.SAVED_MODEL_FILENAME_PB))

# Parse the SavedModel protocol buffer.
saved_model = saved_model_pb2.SavedModel()
if file_io.file_exists(path_to_pb):
    with file_io.FileIO(path_to_pb, "rb") as f:
        file_content = f.read()
    try:
        saved_model.ParseFromString(file_content)
        exit(saved_model)
    except message.DecodeError as e:
        raise IOError(f"Cannot parse file {path_to_pb}: {str(e)}.")
elif file_io.file_exists(path_to_pbtxt):
    with file_io.FileIO(path_to_pbtxt, "rb") as f:
        file_content = f.read()
    try:
        text_format.Merge(file_content.decode("utf-8"), saved_model)
        exit(saved_model)
    except text_format.ParseError as e:
        raise IOError(f"Cannot parse file {path_to_pbtxt}: {str(e)}.")
else:
    raise IOError(
        f"SavedModel file does not exist at: {export_dir}{os.path.sep}"
        f"{{{constants.SAVED_MODEL_FILENAME_PBTXT}|"
        f"{constants.SAVED_MODEL_FILENAME_PB}}}")
