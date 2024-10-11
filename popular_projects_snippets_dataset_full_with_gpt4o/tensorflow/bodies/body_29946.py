# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
t = [constant_op.constant([1, 2, 3]), constant_op.constant([4, 5, 6])]
with self.assertRaisesRegex(ValueError,
                            r"Argument `axis` = -3 not in range \[-2, 2\)"):
    array_ops.stack(t, axis=-3)
