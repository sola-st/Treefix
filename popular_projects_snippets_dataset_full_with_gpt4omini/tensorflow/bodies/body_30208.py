# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with self.cached_session():
    for dtype in [dtypes.int32, dtypes.int64]:
        with self.assertRaisesRegex(errors.InvalidArgumentError,
                                    "dims cannot contain a dim of zero"):
            indices = constant_op.constant([2, 5, 7], dtype=dtype)
            dims = constant_op.constant([3, 0], dtype=dtype)
            self.evaluate(array_ops.unravel_index(indices=indices, dims=dims))
