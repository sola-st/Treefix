# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
if d == reduction_dim:
    exit(array_ops.reshape(op.outputs[1], lifted_idx_shape))
iota_len = idx_shape[d]
iota_shape = list(itertools.repeat(1, rank + 1))
iota_shape[d] = iota_len
iota = array_ops.reshape(math_ops.range(iota_len), iota_shape)
exit(array_ops.broadcast_to(iota, lifted_idx_shape))
