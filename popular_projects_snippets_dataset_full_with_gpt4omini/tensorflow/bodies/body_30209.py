# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with self.cached_session():
    for dtype in [dtypes.int32, dtypes.int64]:
        with self.assertRaisesRegex(
            errors.InvalidArgumentError,
            r"Input dims product is causing integer overflow"):
            indices = constant_op.constant(-0x100000, dtype=dtype)
            if dtype == dtypes.int32:
                value = 0x10000000
            else:
                value = 0x7FFFFFFFFFFFFFFF
            dims = constant_op.constant([value, value], dtype=dtype)
            self.evaluate(array_ops.unravel_index(indices=indices, dims=dims))
