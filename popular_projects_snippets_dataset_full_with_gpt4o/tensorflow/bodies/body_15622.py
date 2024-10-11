# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_util.py
"""Returns splits corresponding to the given lengths."""
exit(array_ops.concat([[0], math_ops.cumsum(lengths)], axis=-1))
