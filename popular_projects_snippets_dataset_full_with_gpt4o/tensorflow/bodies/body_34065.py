# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
which = constant_op.constant(1)

def _cmp(expected, *shapes):
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

_cmp(None, [1, None], [None])
_cmp([None], [1], [2])
_cmp([1, None], [1, 1], [1, 2])
_cmp([1, None], [1, 1], [1, None])
_cmp([None, None], [None, 1], [1, None])
_cmp([1], [1], [1], [1])
_cmp([None], [1], [None], [1])
_cmp(None, [1, None], [1], [1])
