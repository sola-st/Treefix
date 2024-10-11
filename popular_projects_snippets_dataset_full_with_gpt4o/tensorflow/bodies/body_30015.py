# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
for shape in (-1,), (2, -1), (-1, 2), (-2), (-3):
    with self.assertRaises(errors_impl.InvalidArgumentError):
        array_ops.fill(shape, 7)
