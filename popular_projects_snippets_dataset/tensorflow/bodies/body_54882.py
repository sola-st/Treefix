# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
shape_1 = tensor_shape.TensorShape([1, 2, 3])
shape_2 = tensor_shape.TensorShape([None, 2, None])
shape_3 = tensor_shape.TensorShape(None)

self.assertEqual(
    trace_type.deserialize(trace_type.serialize(shape_1)), shape_1)
self.assertEqual(
    trace_type.deserialize(trace_type.serialize(shape_2)), shape_2)
self.assertEqual(
    trace_type.deserialize(trace_type.serialize(shape_3)), shape_3)
