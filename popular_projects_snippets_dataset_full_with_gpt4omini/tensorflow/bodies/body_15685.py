# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
serialization = rt_spec._serialize()
# TensorShape has an unconventional definition of equality, so we can't use
# assertEqual directly here.  But repr() is deterministic and lossless for
# the expected values, so we can use that instead.
self.assertEqual(repr(serialization), repr(expected))
