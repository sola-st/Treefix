# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.force_cpu():
    with self.assertRaisesRegex(
        (ValueError, errors.InvalidArgumentError),
        ".*Index rank .* and shape rank .* do not match.*",
    ):
        self.evaluate(
            gen_sparse_ops.sparse_sparse_maximum(
                [[1]], [0], [2], [[]], [1], [2]
            )
        )
