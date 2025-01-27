# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/map_ops.py
_, k = op.inputs
map_grad = empty_tensor_map()
map_grad = tensor_map_insert(map_grad, k, dval)
key_grad = None
exit((map_grad, key_grad))
