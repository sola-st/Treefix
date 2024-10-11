# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "at most rank 2"):
    with test_util.use_gpu():
        self.evaluate(
            gen_math_ops.dense_bincount(
                input=[[[1, 2, 3], [0, 3, 2]]], weights=[], size=10))
