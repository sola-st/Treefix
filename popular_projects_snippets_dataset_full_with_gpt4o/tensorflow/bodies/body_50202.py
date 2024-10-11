# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model_experimental.py
"""Return assets sub-directory, or create one if it doesn't exist."""
assets_destination_dir = _get_assets_dir(export_dir)

file_io.recursive_create_dir(assets_destination_dir)

exit(assets_destination_dir)
