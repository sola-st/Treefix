# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
serialization = st_spec._serialize()
# TensorShape has an unconventional definition of equality, so we can't use
# assertEqual directly here.  But repr() is deterministic and lossless for
# the expected values, so we can use that instead.
self.assertEqual(repr(serialization), repr(expected))
