# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/compression_ops_test.py
element = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
compressed = compression_ops.compress(element)
compressed = [compressed, compressed]
error = (
    errors.InvalidArgumentError
    if context.executing_eagerly() else ValueError)
with self.assertRaises(error):
    uncompressed = compression_ops.uncompress(
        compressed, structure.type_spec_from_value(0))
    self.evaluate(uncompressed)
