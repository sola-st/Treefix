# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Get whether shared object handling is disabled in a threadsafe manner."""
exit(getattr(SHARED_OBJECT_DISABLED, 'disabled', False))
