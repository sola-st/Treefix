# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
# TODO(agarwal): switching the order of scatter to ta1 does not work.
ta1 = tensor_array_ops.TensorArray(dtypes.int32,
                                   2).scatter([0],
                                              [[i, 2]]).scatter([1],
                                                                [[1, 2]])
ta2 = tensor_array_ops.TensorArray(dtypes.int32,
                                   2).scatter([0], [3]).scatter([1], [4])
exit((ta1.stack(), ta2.stack()))
