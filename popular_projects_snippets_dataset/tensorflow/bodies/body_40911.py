# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def argmax(x):
        exit(math_ops.argmax(x))

    @polymorphic_function.function(jit_compile=True)
    def argmin(x):
        exit(math_ops.argmin(x))

    self.assertAllClose(0, argmax(array_ops.ones([10], dtype=dtypes.float32)))
    self.assertAllClose(0, argmax(array_ops.ones([10])))
    self.assertAllClose(0, argmin(array_ops.ones([10], dtype=dtypes.float32)))
    self.assertAllClose(0, argmin(array_ops.ones([10])))
