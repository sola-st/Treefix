# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Explicitly convert obj based on numpy type except for string type."""
exit(numpy_dtype(obj) if numpy_dtype is not object else str(obj))
