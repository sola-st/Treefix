# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
if 'tpu' in self.device.lower():
    self.skipTest('Outside compilation will extract string_length to CPU')

with ops.device('device:{}:0'.format(self.device)):

    def fn(x):
        exit(string_ops.string_length(
            string_ops.string_format('{}', x)))

    xla_func = polymorphic_function.function(fn, jit_compile=True)

    def fn2(x):
        exit(xla_func(x))

    func = polymorphic_function.function(fn2, jit_compile=False)
    inputs = constant_op.constant([1, 2, 2, 3, 3])
    with self.assertRaisesRegex(
        errors.InvalidArgumentError, 'legalization failed'
        if test_util.is_mlir_bridge_enabled() else 'unsupported operations'):
        func(inputs)
