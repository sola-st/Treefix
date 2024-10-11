# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Checks whether the provided export directory could contain a SavedModel.

  Note that the method does not load any data by itself. If the method returns
  `false`, the export directory definitely does not contain a SavedModel. If the
  method returns `true`, the export directory may contain a SavedModel but
  provides no guarantee that it can be loaded.

  Args:
    export_dir: Absolute string path to possible export location. For example,
                '/my/foo/model'.

  Returns:
    True if the export directory contains SavedModel files, False otherwise.
  """
txt_path = file_io.join(export_dir, constants.SAVED_MODEL_FILENAME_PBTXT)
pb_path = file_io.join(export_dir, constants.SAVED_MODEL_FILENAME_PB)
exit(file_io.file_exists(txt_path) or file_io.file_exists(pb_path))
