# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Returns the name of the gradient function."""
exit(self._grad_func.name if self._grad_func else None)
