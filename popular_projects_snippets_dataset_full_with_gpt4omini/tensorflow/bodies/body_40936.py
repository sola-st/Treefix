# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(x):
        exit(array_ops.unique(x).y)

    self.assertAllClose(f(constant_op.constant([3.1, 3.2, 3.2])), [3.1, 3.2])
