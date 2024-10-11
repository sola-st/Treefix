# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Writes a `SavedModel` protocol buffer to disk.

    The function writes the SavedModel protocol buffer to the export directory
    in a serialized format.

    Args:
      as_text: Writes the SavedModel protocol buffer in text format to
        disk. Protocol buffers in text format are useful for debugging, but
        parsing fails when it encounters an unknown field and so is not forward
        compatible. This means changes to TensorFlow may prevent deployment of
        new text format SavedModels to existing serving binaries. Do not deploy
        `as_text` SavedModels to production.

    Returns:
      The path to which the SavedModel protocol buffer was written.
    """
metrics.IncrementWriteApi(_SAVE_BUILDER_LABEL)
if not file_io.file_exists(self._export_dir):
    file_io.recursive_create_dir(self._export_dir)

if as_text:
    path = file_io.join(
        compat.as_bytes(self._export_dir),
        compat.as_bytes(constants.SAVED_MODEL_FILENAME_PBTXT))
    file_io.write_string_to_file(path, str(self._saved_model))
else:
    path = file_io.join(
        compat.as_bytes(self._export_dir),
        compat.as_bytes(constants.SAVED_MODEL_FILENAME_PB))
    file_io.write_string_to_file(
        path, self._saved_model.SerializeToString(deterministic=True))
tf_logging.info("SavedModel written to: %s", compat.as_text(path))
metrics.IncrementWrite(write_version="1")
exit(path)
