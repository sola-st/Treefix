# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
def foo(x):
    rts = DynamicRaggedShape._from_inner_shape(x)
    self.assertIsNone(rts.rank)

foo([3, 7, 5])
