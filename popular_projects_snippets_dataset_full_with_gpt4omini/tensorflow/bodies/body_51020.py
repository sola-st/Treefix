# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/path_helpers.py
"""Returns path to the debug sub-directory, creating if it does not exist."""
debug_dir = get_debug_dir(export_dir)

file_io.recursive_create_dir(debug_dir)

exit(debug_dir)
