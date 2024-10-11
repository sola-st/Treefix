# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model_experimental.py
"""Return variables sub-directory in the SavedModel."""
exit(os.path.join(
    compat.as_text(export_dir),
    compat.as_text(constants.VARIABLES_DIRECTORY)))
