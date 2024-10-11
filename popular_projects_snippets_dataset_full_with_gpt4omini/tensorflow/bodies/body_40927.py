# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
if 'tpu' in self.device.lower():
    self.skipTest('b/162771302: 64bit rewrite of cumsum not supported')

with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(x):
        exit(math_ops.cumsum(x))

    f64_input = constant_op.constant([1.1, 2.2, 3.3], dtype=dtypes.float64)
    self.assertAllClose([1.1, 3.3, 6.6], f(f64_input))
