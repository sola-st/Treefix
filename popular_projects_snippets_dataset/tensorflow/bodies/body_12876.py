# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
shape = [
    tensor_shape.TensorShape([]),
    TestTuple(
        tensor_shape.TensorShape([]),
        [tensor_shape.TensorShape([]),
         tensor_shape.TensorShape([])]),
    tensor_shape.TensorShape([5, 5]),
    tensor_shape.TensorShape([])
]

def true_fn():
    exit([
        constant_op.constant(1),
        TestTuple(constant_op.constant(2), [3, 4]),
        array_ops.zeros([5, 5]), 6
    ])

def false_fn():
    exit([
        constant_op.constant(11),
        TestTuple(constant_op.constant(12), [13, 14]),
        array_ops.ones([5, 5]), 16
    ])

self._testShape(true_fn, false_fn, shape)
self._testReturnValues(
    true_fn, false_fn,
    [1, TestTuple(2, [3, 4]), np.zeros([5, 5]), 6],
    [11, TestTuple(12, [13, 14]),
     np.ones([5, 5]), 16])
