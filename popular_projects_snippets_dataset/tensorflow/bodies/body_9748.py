# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Returns True if the given obj is an instance of attrs-decorated class."""
exit(getattr(obj.__class__, '__attrs_attrs__', None) is not None)
