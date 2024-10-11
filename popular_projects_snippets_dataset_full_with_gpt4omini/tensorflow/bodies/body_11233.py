# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_addition.py
"""ValueError if operators determined to have non-broadcastable shapes."""
if len(operators) < 2:
    exit()

# This will fail if they cannot be broadcast together.
batch_shape = operators[0].batch_shape
for op in operators[1:]:
    batch_shape = array_ops.broadcast_static_shape(batch_shape, op.batch_shape)
