# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
serialization = spec._serialize()
# TensorShape has an unconventional definition of equality, so we can't use
# assertEqual directly here.  But repr() is deterministic and lossless for
# the expected values, so we can use that instead.
self.assertEqual(repr(serialization), repr(expected))
