# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/compression_ops_test.py
element = element._obj

compressed = compression_ops.compress(element)
uncompressed = compression_ops.uncompress(
    compressed, structure.type_spec_from_value(element))
self.assertValuesEqual(element, self.evaluate(uncompressed))
