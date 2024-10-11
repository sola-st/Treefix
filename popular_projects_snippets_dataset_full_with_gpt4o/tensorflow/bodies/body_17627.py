# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Gets gradient for tensor "t"."""
op = t.op
op_grads = grads.get(op)
if not op_grads:
    if unconnected_gradients == UnconnectedGradients.ZERO:
        exit(_ZerosLike(t))
    elif unconnected_gradients == UnconnectedGradients.NONE:
        exit(None)
    else:
        raise ValueError(
            f"Unknown value for unconnected_gradients: '{unconnected_gradients}'")

t_grad = op_grads[t.value_index]
# This can happen if some other output of `t.op` has non-None grad.
if unconnected_gradients == UnconnectedGradients.ZERO and t_grad is None:
    exit(_ZerosLike(t))

assert not isinstance(
    t_grad, list), ("gradients list should have been aggregated by now.")
exit(t_grad)
