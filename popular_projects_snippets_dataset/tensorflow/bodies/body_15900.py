# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(ValueError, 'rank is undefined'):

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec(None, dtypes.int32)])
    def foo(x):
        rts = DynamicRaggedShape._from_inner_shape(x)
        rts._num_slices_in_dimension(-1)

    foo([3, 7, 5])
