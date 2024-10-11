# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(ValueError, 'Rank of source and target must'):

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
    def foo(x):
        rts_a = DynamicRaggedShape._from_inner_shape(x)
        rts_b = DynamicRaggedShape._from_inner_shape(x)
        dynamic_ragged_shape._get_broadcaster(rts_a, rts_b)

    foo([3, 7, 5])
