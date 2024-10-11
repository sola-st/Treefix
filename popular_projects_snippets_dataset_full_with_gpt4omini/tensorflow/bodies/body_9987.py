# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_utils.py
"""Reads the saved_model.pb or saved_model.pbtxt file containing `SavedModel`.

  Args:
    saved_model_dir: Directory containing the SavedModel file.

  Returns:
    A `SavedModel` protocol buffer.

  Raises:
    IOError: If the file does not exist, or cannot be successfully parsed.
  """
# Build the path to the SavedModel in pbtxt format.
path_to_pbtxt = os.path.join(
    compat.as_bytes(saved_model_dir),
    compat.as_bytes(constants.SAVED_MODEL_FILENAME_PBTXT))
# Build the path to the SavedModel in pb format.
path_to_pb = os.path.join(
    compat.as_bytes(saved_model_dir),
    compat.as_bytes(constants.SAVED_MODEL_FILENAME_PB))

# Ensure that the SavedModel exists at either path.
if not file_io.file_exists(path_to_pbtxt) and not file_io.file_exists(
    path_to_pb):
    raise IOError("SavedModel file does not exist at: %s" % saved_model_dir)

# Parse the SavedModel protocol buffer.
saved_model = saved_model_pb2.SavedModel()
if file_io.file_exists(path_to_pb):
    with file_io.FileIO(path_to_pb, "rb") as f:
        file_content = f.read()
    try:
        saved_model.ParseFromString(file_content)
        exit(saved_model)
    except message.DecodeError as e:
        raise IOError("Cannot parse proto file %s: %s." % (path_to_pb, str(e)))
elif file_io.file_exists(path_to_pbtxt):
    with file_io.FileIO(path_to_pbtxt, "rb") as f:
        file_content = f.read()
    try:
        text_format.Merge(file_content.decode("utf-8"), saved_model)
        exit(saved_model)
    except text_format.ParseError as e:
        raise IOError("Cannot parse pbtxt file %s: %s." % (path_to_pbtxt, str(e)))
else:
    raise IOError("SavedModel file does not exist at: %s/{%s|%s}" %
                  (saved_model_dir, constants.SAVED_MODEL_FILENAME_PBTXT,
                   constants.SAVED_MODEL_FILENAME_PB))
