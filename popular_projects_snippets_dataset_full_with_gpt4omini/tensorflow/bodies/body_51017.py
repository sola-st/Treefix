# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/path_helpers.py
"""Return the variables path, used as the prefix for checkpoint files."""
exit(file_io.join(
    compat.as_text(get_variables_dir(export_dir)),
    compat.as_text(constants.VARIABLES_FILENAME)))
