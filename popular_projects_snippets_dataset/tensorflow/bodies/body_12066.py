# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Returns conj(unshuffle(grad))."""
p = op.inputs[1]
exit([
    array_ops.transpose(
        grad, array_ops.invert_permutation(p), conjugate=True), None
])
