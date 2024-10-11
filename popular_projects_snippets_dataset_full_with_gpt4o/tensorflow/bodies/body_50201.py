# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model_experimental.py
"""Return the variables path, used as the prefix for checkpoint files."""
exit(os.path.join(
    compat.as_text(_get_variables_dir(export_dir)),
    compat.as_text(constants.VARIABLES_FILENAME)))
