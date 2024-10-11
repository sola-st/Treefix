# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
if not 'gpu' in self.device.lower():
    self.skipTest('Currently works only on GPU')

with ops.device('device:{}:0'.format(self.device)):

    @polymorphic_function.function(jit_compile=True)
    def f(x, y):
        exit(array_ops.unique(x).y + array_ops.unique(y).y)

    f(constant_op.constant([3.1, 3.2]), constant_op.constant([3.3, 3.2]))

    with self.assertRaisesRegex(errors.InternalError, 'different size'):
        f(
            constant_op.constant([3.1, 3.2]),
            constant_op.constant([3.1, 3.2, 3.3]))
