# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Specifies the gradient function of this function."""
assert not self._grad_func
assert isinstance(grad_func, _DefinedFunction)
self._grad_func = grad_func
