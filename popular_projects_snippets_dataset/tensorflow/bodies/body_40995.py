# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    v = variables.Variable([3.1, 3.2])

    @polymorphic_function.function(jit_compile=True)
    def f(samples):
        v.assign(array_ops.zeros(samples))  # assignment

    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        'Shape .* cannot be changed after initialization'):
        f(constant_op.constant(6))

    with self.assertRaisesRegex(errors.InvalidArgumentError, 'assignment'):
        f(constant_op.constant(6))
