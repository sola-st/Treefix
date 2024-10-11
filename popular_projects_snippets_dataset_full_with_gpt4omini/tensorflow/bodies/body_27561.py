# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/compression_ops_test.py
element = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
compressed = compression_ops.compress(element)
with self.assertRaisesRegex(errors.FailedPreconditionError,
                            "but got a tensor of type string"):
    uncompressed = compression_ops.uncompress(
        compressed, structure.type_spec_from_value(0))
    self.evaluate(uncompressed)
