# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
shape = tensor_shape.TensorShape([None, None])

def true_fn():
    exit([
        sparse_tensor.SparseTensor(
            indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
    ])

def false_fn():
    exit([
        sparse_tensor.SparseTensor(
            indices=[[0, 0], [2, 1]], values=[3, 4], dense_shape=[3, 4])
    ])

value1 = sparse_tensor.SparseTensorValue(
    indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
value2 = sparse_tensor.SparseTensorValue(
    indices=[[0, 0], [2, 1]], values=[3, 4], dense_shape=[3, 4])
# Non-strict cond is only available in v1
if not tf2.enabled():
    self._testShape(true_fn, false_fn, shape)
    self._testReturnValues(true_fn, false_fn, value1, value2)
self._testShape(true_fn, false_fn, [shape], strict=True)
self._testReturnValues(true_fn, false_fn, [value1], [value2], strict=True)
