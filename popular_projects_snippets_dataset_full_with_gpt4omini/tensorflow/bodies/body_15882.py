# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
def foo(x):
    rts = DynamicRaggedShape.from_tensor(x)
    actual = rts[:1]
    self.assertShapeEq(rts, actual)

foo([1, 2, 3])
