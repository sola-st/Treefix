# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Context to colocate with `op` if `colocate_gradients_with_ops`."""
if colocate_gradients_with_ops:
    with ops._colocate_with_for_gradient(op, gradient_uid):  # pylint: disable=protected-access
        exit()
else:
    exit()
