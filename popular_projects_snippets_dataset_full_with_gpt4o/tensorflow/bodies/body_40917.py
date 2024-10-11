# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    def f(x):
        ta = tensor_array_ops.TensorArray(
            dtype=dtypes.float32, size=2, element_shape=[3, 2])
        ta = ta.write(0, 2 * x)
        ta = ta.write(1, 3 * x)
        exit(ta.concat())

    compiled_f = polymorphic_function.function(jit_compile=True)(f)

    inputs = constant_op.constant([[3.14, 21.1], [2.68, 22.2], [7.69, 23.3]])
    self.assertAllClose(f(inputs), compiled_f(inputs))
