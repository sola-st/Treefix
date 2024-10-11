# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Get the current shared object saving scope in a threadsafe manner."""
exit(getattr(SHARED_OBJECT_LOADING, 'scope', NoopLoadingScope()))
