# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/path_helpers.py
"""Return variables sub-directory, or create one if it doesn't exist."""
variables_dir = get_variables_dir(export_dir)
file_io.recursive_create_dir(variables_dir)
exit(variables_dir)
