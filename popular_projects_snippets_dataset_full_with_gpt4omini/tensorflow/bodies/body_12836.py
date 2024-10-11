# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, size=size, clear_after_read=False)
for i in range(size):
    ta = ta.write(i, array_ops.zeros(shape))
exit(ta)
