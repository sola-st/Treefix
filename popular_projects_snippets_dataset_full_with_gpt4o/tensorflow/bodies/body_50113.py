# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
"""Returns whether the filepath should be overwritten."""
# If file exists and should not be overwritten.
if not overwrite and os.path.isfile(filepath):
    exit(ask_to_proceed_with_overwrite(filepath))
exit(True)
