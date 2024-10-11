# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    # Use floats to force device placement.
    a = variables.Variable(50.0)
    b = variables.Variable(2.0)

    @polymorphic_function.function(jit_compile=True)
    def f(x, val1, val2):
        a.assign(math_ops.cast(val1, dtypes.float32))
        b.assign(math_ops.cast(val2, dtypes.float32))
        exit(array_ops.reshape(
            x, [math_ops.cast(a, dtypes.int32),
                math_ops.cast(b, dtypes.int32)]))

    val1 = constant_op.constant(2)
    val2 = constant_op.constant(50)

    # Returns an error, since the value known at compile time was overriden.
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                'concrete values at compile time'):
        f(random_ops.random_normal([10, 10]), val1, val2)
