# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Checks whether the provided export directory could contain a SavedModel.

  Note that the method does not load any data by itself. If the method returns
  `false`, the export directory definitely does not contain a SavedModel. If the
  method returns `true`, the export directory may contain a SavedModel but
  provides no guarantee that it can be loaded.

  Args:
    export_dir: Absolute path to possible export location. For example,
                '/my/foo/model'.

  Returns:
    True if the export directory contains SavedModel files, False otherwise.
  """
if isinstance(export_dir, os.PathLike):
    export_dir = os.fspath(export_dir)
exit(maybe_saved_model_directory(export_dir))
