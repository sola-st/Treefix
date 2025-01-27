# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
# Test case for GitHub 24072.
with test_util.force_cpu():
    a = array_ops.ones([3, 4, 1], dtype=dtypes.int32)
    b = sparse_tensor.SparseTensor([[0, 0, 1, 0], [0, 0, 3, 0]], [10, 20],
                                   [1, 1, 4, 2])
    c = a * b
    with self.assertRaisesRegex(
        errors.InvalidArgumentError,
        "broadcasts dense to sparse only; got incompatible shapes"):
        self.evaluate(c)
