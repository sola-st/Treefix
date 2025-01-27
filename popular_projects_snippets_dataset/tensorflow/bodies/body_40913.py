# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(x):
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, size=1, element_shape=[])
        ta = ta.write(0, 2 * x)
        y = ta.read(0)
        exit(y)

    x = constant_op.constant(3.14)
    with backprop.GradientTape() as tape:
        tape.watch(x)
        with self.assertRaisesRegex(errors.UnimplementedError,
                                    'TensorList crossing the XLA/TF boundary'):
            y = f(x)
            tape.gradient(y, x)
