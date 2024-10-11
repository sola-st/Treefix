# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Gets all gradients for op."""
if op in grads:
    exit(grads[op])
else:
    exit([[] for _ in range(len(op.outputs))])
