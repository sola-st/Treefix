# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
spec = TwoTensorsSpec([5, 3], dtypes.int32, None, dtypes.bool)
self.assertEqual(
    repr(spec),
    "TwoTensorsSpec(%r, %r, %r, %r, %r)" %
    (tensor_shape.TensorShape([5, 3]), dtypes.int32,
     tensor_shape.TensorShape(None), dtypes.bool, "red"))
