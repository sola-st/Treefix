# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack.py
"""Remove last-inserted object and return it, without filename/line info."""
exit(self._stack.pop().obj)
