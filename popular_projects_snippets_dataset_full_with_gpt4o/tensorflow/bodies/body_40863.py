# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    def fn(x):
        exit(string_ops.string_length(
            string_ops.string_format('{}', x)))

    xla_func = polymorphic_function.function(fn, jit_compile=True)

    with self.assertRaisesRegex(
        errors.InvalidArgumentError, 'legalization failed'
        if test_util.is_mlir_bridge_enabled() else 'unsupported operations'):
        xla_func(constant_op.constant([3.1, 3.2]))
