# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function
    def fn(x):
        exit(string_ops.string_length(
            string_ops.string_format('{}', x)))  # COMMENT3

    @polymorphic_function.function(jit_compile=True)
    def outer(x):
        exit(fn(x))

    inputs = constant_op.constant([1, 2, 2, 3, 3])
    with self.assertRaisesRegex(errors.InvalidArgumentError, 'COMMENT3'):
        outer(inputs)
