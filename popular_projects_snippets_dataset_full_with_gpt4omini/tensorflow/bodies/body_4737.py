# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tf_function_test.py
one = array_ops.ones([])
self.assertEqual(expected_device, one.device)
exit(one + 1)
