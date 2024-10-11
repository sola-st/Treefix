# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    # Use floats to force device placement.
    a = variables.Variable(50.0)
    b = variables.Variable(2.0)

    @polymorphic_function.function(jit_compile=True)
    def f(x, val1, val2):
        out = array_ops.reshape(
            x, [math_ops.cast(a, dtypes.int32),
                math_ops.cast(b, dtypes.int32)])
        a.assign(math_ops.cast(val1, dtypes.float32))
        b.assign(math_ops.cast(val2, dtypes.float32))
        exit(out)

    val1 = constant_op.constant(2)
    val2 = constant_op.constant(50)

    # OK since the write happens after the reshape.
    out = f(random_ops.random_normal([10, 10]), val1, val2)
    self.assertEqual(out.shape[0], 50)
    self.assertEqual(out.shape[1], 2)
