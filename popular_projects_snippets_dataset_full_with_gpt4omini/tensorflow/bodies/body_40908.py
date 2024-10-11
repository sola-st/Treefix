# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
if 'tpu' in self.device.lower():
    self.skipTest('b/162799319: Cannot resolve constant on TPU')

with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f():
        exit(constant_op.constant([0, 2, 1], dtype=dtypes.int32))

    @polymorphic_function.function(jit_compile=True)
    def g(a, b):
        exit(array_ops.transpose(a, b))

    @polymorphic_function.function
    def z():
        exit(g(array_ops.ones([3, 4, 3], dtype=dtypes.float32), f()))

    z()
