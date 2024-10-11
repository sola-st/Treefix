# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
q_u_u = data_flow_ops.PaddingFIFOQueue(
    10, [dtypes_lib.float32, dtypes_lib.int32],
    [tensor_shape.TensorShape([None]), tensor_shape.TensorShape([None])])
q_u_f = data_flow_ops.PaddingFIFOQueue(
    10, [dtypes_lib.float32, dtypes_lib.int32],
    [tensor_shape.TensorShape([None]), tensor_shape.TensorShape([1, 2])])
q_f_f = data_flow_ops.PaddingFIFOQueue(
    10, [dtypes_lib.float32, dtypes_lib.int32],
    [tensor_shape.TensorShape([3, 4]), tensor_shape.TensorShape([1, 2])])
which = constant_op.constant(1)

s_cmp_1 = data_flow_ops.QueueBase.from_list(which,
                                            [q_u_u, q_u_u, q_u_u]).shapes
self.assertEqual([1, 1], [x.ndims for x in s_cmp_1])
self.assertEqual([None, None], [x.as_list()[0] for x in s_cmp_1])

s_cmp_2 = data_flow_ops.QueueBase.from_list(which,
                                            [q_u_u, q_u_u, q_u_f]).shapes
self.assertEqual([1, None], [x.ndims for x in s_cmp_2])
self.assertEqual([None], s_cmp_2[0].as_list())

s_cmp_3 = data_flow_ops.QueueBase.from_list(which, [q_f_f, q_f_f]).shapes
self.assertEqual([2, 2], [x.ndims for x in s_cmp_3])
self.assertEqual([[3, 4], [1, 2]], [x.as_list() for x in s_cmp_3])
