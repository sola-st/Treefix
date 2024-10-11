# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
input_bytes = ["1"]
# Different error messages depending on shape inference vs kernel.
with self.assertRaisesRegex(
    (ValueError, errors_impl.InvalidArgumentError),
    "must be a multiple of|evenly divisible by",
):
    self.evaluate(
        self._decode_v2(input_bytes, fixed_length=7, dtype=dtypes.float32)
    )
