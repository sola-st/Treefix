# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(ValueError,
                            'Unable to broadcast: unknown rank'):

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
    def foo(x):
        a = DynamicRaggedShape._from_inner_shape(x)
        b = DynamicRaggedShape._from_inner_shape([1, 1, 1])
        dynamic_ragged_shape.broadcast_dynamic_shape_extended(a, b)

    foo([3, 7, 5])
