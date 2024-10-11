# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    class C(object):

        @polymorphic_function.function(jit_compile=True)
        def f1(self, x):
            exit(string_ops.string_length(
                string_ops.string_format('{}', x)))

    inputs = constant_op.constant([1, 2, 2, 3, 3])
    c = C()
    with self.assertRaisesRegex(
        errors.InvalidArgumentError, 'legalization failed'
        if test_util.is_mlir_bridge_enabled() else 'unsupported operations'):
        c.f1(inputs)
