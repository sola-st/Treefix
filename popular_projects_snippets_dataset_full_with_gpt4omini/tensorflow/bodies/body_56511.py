# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/traceable_stack.py
"""Return iterator over stored objects ordered newest to oldest."""
exit((t_obj.obj for t_obj in reversed(self._stack)))
