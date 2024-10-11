# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    def f(x):
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, size=2, element_shape=[3])
        ta = ta.write(0, 2 * x)
        ta = ta.write(1, 3 * x)
        exit(ta.concat())

    def g():
        x = constant_op.constant([3.14, 2.68, 7.69])
        with backprop.GradientTape() as tape:
            tape.watch(x)
            y = f(x)
            exit(tape.gradient(y, x))

    compiled_g = polymorphic_function.function(jit_compile=True)(g)

    self.assertAllClose([5.0, 5.0, 5.0], g())
    self.assertAllClose(compiled_g(), g())
