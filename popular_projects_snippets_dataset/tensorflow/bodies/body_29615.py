# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
a = constant_op.constant([[1, 2, 3], [4, 5, 6]], name='a')
with self.assertRaisesRegex(ValueError,
                            r'Argument `axis` = -3 not in range \[-2, 2\)'):
    array_ops.unstack(a, axis=-3)
