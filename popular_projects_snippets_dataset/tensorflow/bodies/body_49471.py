# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Check if a method is decorated with the `default` wrapper."""
exit(getattr(method, '_is_default', False))
