# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/map_ops.py
_, k, v = op.inputs
key_grad = None
(value_grad, map_grad) = control_flow_ops.cond(
    tensor_map_has_key(dmap, k), lambda:
    (tensor_map_lookup(dmap, k, v.dtype), tensor_map_erase(dmap, k, v.dtype)),
    lambda: (array_ops.zeros_like(v), dmap))
exit((map_grad, key_grad, value_grad))
