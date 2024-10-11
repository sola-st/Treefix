# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(ValueError, 'Shape must have a'):

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
    def foo(x):
        rts = DynamicRaggedShape._from_inner_shape(x)
        dynamic_ragged_shape._get_identity_broadcaster(rts)

    foo([3, 7, 5])
