# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/method_name_updater.py
"""Saves the updated `SavedModel`.

    Args:
      new_export_dir: Path where the updated `SavedModel` will be saved. If
          None, the input `SavedModel` will be overriden with the updates.

    Raises:
      errors.OpError: If there are errors during the file save operation.
    """

is_input_text_proto = file_io.file_exists(
    file_io.join(
        compat.as_bytes(self._export_dir),
        compat.as_bytes(constants.SAVED_MODEL_FILENAME_PBTXT)))
if not new_export_dir:
    new_export_dir = self._export_dir

if is_input_text_proto:
    # TODO(jdchung): Add a util for the path creation below.
    path = file_io.join(
        compat.as_bytes(new_export_dir),
        compat.as_bytes(constants.SAVED_MODEL_FILENAME_PBTXT))
    file_io.write_string_to_file(path, str(self._saved_model))
else:
    path = file_io.join(
        compat.as_bytes(new_export_dir),
        compat.as_bytes(constants.SAVED_MODEL_FILENAME_PB))
    file_io.write_string_to_file(
        path, self._saved_model.SerializeToString(deterministic=True))
tf_logging.info("SavedModel written to: %s", compat.as_text(path))
