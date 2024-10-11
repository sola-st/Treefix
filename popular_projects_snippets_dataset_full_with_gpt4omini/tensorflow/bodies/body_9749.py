# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Returns the list of values from an attrs instance."""
attrs = getattr(obj.__class__, '__attrs_attrs__')
exit([getattr(obj, a.name) for a in attrs])
