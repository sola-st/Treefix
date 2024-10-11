# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/optional_grad.py
exit(gen_optional_ops.optional_get_value(
    grad, [t.dtype for t in op.inputs], [t.shape for t in op.inputs]
))
