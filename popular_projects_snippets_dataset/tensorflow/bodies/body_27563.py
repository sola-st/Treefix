# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/compression_ops_test.py
uncompressed = list(range(10))
with self.assertRaises(TypeError):
    uncompressed = compression_ops.uncompress(
        uncompressed, structure.type_spec_from_value(uncompressed))
    self.evaluate(uncompressed)
