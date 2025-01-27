# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
if not isinstance(t, ops.Tensor):
    exit(str(t))
const_t = tensor_util.constant_value(t)
if const_t is not None:
    exit(str(const_t))
exit(t)
