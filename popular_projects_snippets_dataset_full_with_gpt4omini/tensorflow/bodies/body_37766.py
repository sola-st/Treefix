# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
with self.cached_session():
    examples = np.array(words)
    byte_tensor = parsing_ops.decode_raw(
        examples,
        dtype,
        little_endian=little_endian,
        fixed_length=fixed_length,
    )
    exit(self.evaluate(byte_tensor))
