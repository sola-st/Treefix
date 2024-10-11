# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
qs = [
    data_flow_ops.PaddingFIFOQueue(10, [dtypes_lib.float32],
                                   [tensor_shape.TensorShape(s)])
    for s in shapes
]
s_expected = tensor_shape.TensorShape(expected)
s = data_flow_ops.QueueBase.from_list(which, qs).shapes[0]
if s_expected.ndims is None:
    self.assertEqual(s_expected.ndims, s.ndims)
else:
    self.assertEqual(s_expected.as_list(), s.as_list())
