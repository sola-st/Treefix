# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/path_helpers.py
"""Return variables sub-directory in the SavedModel."""
exit(file_io.join(
    compat.as_text(export_dir), compat.as_text(constants.VARIABLES_DIRECTORY)))
