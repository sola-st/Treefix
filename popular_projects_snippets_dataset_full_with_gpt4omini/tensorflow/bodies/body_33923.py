# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/array_ops_test.py
lengths = array_ops.placeholder(dtype=dtypes.int32)
res = array_ops.sequence_mask(lengths)
self.assertEqual(res.shape, None)  # pylint: disable=g-generic-assert
