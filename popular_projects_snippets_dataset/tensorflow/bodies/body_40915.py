# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    def f(x):
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, size=2, element_shape=[3])
        ta = ta.write(0, 2 * x)
        ta = ta.write(1, 3 * x)
        exit(ta.concat())

    compiled_f = polymorphic_function.function(jit_compile=True)(f)

    inputs = constant_op.constant([3.14, 2.68, 7.69])

    self.assertAllClose([6.28, 5.36, 15.38, 9.42, 8.04, 23.07], f(inputs))

    self.assertAllClose(compiled_f(inputs), f(inputs))
