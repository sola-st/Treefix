# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
# TODO(b/168657656): This function should be replaced by
# tensordot(axis=1) once MatMul has int32 XLA kernel.
b = array_ops.broadcast_to(b, array_ops.shape(a))
exit(math_ops.reduce_sum(a * b, axis=-1))
