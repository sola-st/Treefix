# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
# TODO(agarwal): switching the order of writes to ta1 does not work.
ta1 = tensor_array_ops.TensorArray(dtypes.int32, 2).write(0,
                                                          i).write(1, 1)
ta2 = tensor_array_ops.TensorArray(dtypes.int32, 1).write(0, 1)
exit((ta1.stack(), ta2.stack()))
