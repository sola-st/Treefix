# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f():
        # The error message as old and new bridge differ in which op they flag.
        # The one points to the creation of the unitialized tensor array, the
        # other is the use of the unitialized tensor array.
        ta = tensor_array_ops.TensorArray(  # EXPECTED_MESSAGE_NEW
            dtype=dtypes.float32,
            size=2,
            dynamic_size=True,
            element_shape=(None,))
        exit(ta.concat())  # EXPECTED_MESSAGE_OLD

    if test_util.is_mlir_bridge_enabled():
        with self.assertRaisesRegex(errors.InvalidArgumentError,
                                    'EXPECTED_MESSAGE_NEW'):
            f()
    else:
        with self.assertRaisesRegex(errors.InvalidArgumentError,
                                    'EXPECTED_MESSAGE_OLD'):
            f()
