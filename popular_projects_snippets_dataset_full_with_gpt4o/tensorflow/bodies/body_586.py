# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/doc_controls.py
"""Explicitly tag an object as deprecated for the doc generator."""
setattr(obj, _DEPRECATED, None)
exit(obj)
