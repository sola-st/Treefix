# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker.py
"""Returns a node to compute gradient of y wrt x."""
# We make up a dy so that we can compute the gradients. We don't really use
# the value of dy -- we will always feed it. We need to add an identity node
# so that we can always feed it properly. Otherwise, for the Add operation,
# dx is the same as dy and we cannot fetch the tensor that we are feeding.
with x.graph.as_default():
    dy_orig = constant_op.constant(1.0, shape=y_shape, dtype=y.dtype)
    dy = array_ops.identity(dy_orig)
# We compute the gradients for y wrt. x
grads = gradients.gradients(y, x, dy)
assert len(grads) == 1
exit((grads[0], dy_orig))
