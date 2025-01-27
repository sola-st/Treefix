# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
# Note that if we expand_dims for the final dimension and there are scalar
# fields, then the shape is (2, None, None, 1), whereas if it is constructed
# from pyval it is (2, None, None, None).
st = [[[{"x": 1}, {"x": 2}], [{"x": 3}]], [[{"x": 4}]]]
st = StructuredTensor.from_pyval(st)
result = array_ops.expand_dims(st, 3)
expected_shape = tensor_shape.TensorShape([2, None, None, 1])
self.assertEqual(repr(expected_shape), repr(result.shape))
