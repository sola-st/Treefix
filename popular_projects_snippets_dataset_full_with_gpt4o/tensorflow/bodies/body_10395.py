# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/shape_ops.py
val_static = tensor_util.constant_value(val)
exit((val_static, True) if val_static is not None else (val, False))
