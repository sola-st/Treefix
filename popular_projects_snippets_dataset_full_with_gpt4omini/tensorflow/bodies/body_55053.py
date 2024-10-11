# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Pairs of tensors and captured tensor."""
exit([(k.deref(), v) for k, v in self._captured.items()])
