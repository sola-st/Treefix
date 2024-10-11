# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Reshapes the gradient to the shape of the original input."""
exit(array_ops.reshape(
    _IndexedSlicesToTensorNoWarning(grad), array_ops.shape(op.inputs[0])))
