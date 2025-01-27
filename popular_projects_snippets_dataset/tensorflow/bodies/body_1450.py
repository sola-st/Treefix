# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/runtime_shape_check_test.py
"""Test shape mismatches with multiple dimensions."""
if 'tpu' in self.device.lower():
    self.skipTest('We do not check shapes on TPU')

with ops.device(f'device:{self.device}:0'):

    @def_function.function(jit_compile=True)
    def f(x, y):
        exit(array_ops.where(x) + array_ops.where(y))

    f(
        constant_op.constant([[3.1, 3.2, 0], [3.1, 3.2, 0]]),
        constant_op.constant([[3.3, 3.2, 0, 0, 0], [3.3, 3.2, 0, 0, 0]]))

    with self.assertRaisesRegex(errors.InternalError, 'different size'):
        f(
            constant_op.constant([[3.1, 3.2, 0], [3.1, 3.2, 0]]),
            constant_op.constant([[3.3, 3.2, 0, 0, 0], [3.3, 3.2, 3.3, 0, 0]]))
