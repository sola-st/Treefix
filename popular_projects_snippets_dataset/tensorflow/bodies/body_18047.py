# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
ta1 = tensor_array_ops.TensorArray(
    dtypes.int32, 2, clear_after_read=False).write(0, i).write(1, 1)
ta2 = tensor_array_ops.TensorArray(
    dtypes.int32, 2, clear_after_read=False).write(0, 1).write(1, 2)
# TODO(agarwal): ta1.read(i) currently is not supported.
exit((ta1.read(0), ta2.read(0), ta2.read(i)))
