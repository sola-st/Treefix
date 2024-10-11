# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
result = nest.pack_sequence_as(
    structure, sequence, expand_composites=expand_composites)
self.assertEqual(result, expected)
