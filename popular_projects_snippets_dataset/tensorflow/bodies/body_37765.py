# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
with self.cached_session():
    examples = np.array(words)
    example_tensor = constant_op.constant(
        examples, shape=examples.shape, dtype=dtypes.string)
    byte_tensor = parsing_ops.decode_raw_v1(example_tensor, dtypes.uint8)
    exit(self.evaluate(byte_tensor))
