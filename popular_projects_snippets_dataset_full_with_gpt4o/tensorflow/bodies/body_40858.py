# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
if 'tpu' in self.device.lower():
    self.skipTest('b/162800687: Inner function runs on host')

with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def fn(x, a):
        exit(x + a)

    @polymorphic_function.function(jit_compile=False)
    def fn2(x, a):
        exit(fn(x, a))

    inputs = constant_op.constant([1, 2, 2, 3, 3])
    self.assertAllClose([2, 3, 3, 4, 4], fn2(inputs, 1))
