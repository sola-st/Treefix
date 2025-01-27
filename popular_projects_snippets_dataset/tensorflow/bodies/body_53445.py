# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Raises a helpful error."""
raise TypeError("can't convert Operation '{}' to Tensor".format(self.name))
