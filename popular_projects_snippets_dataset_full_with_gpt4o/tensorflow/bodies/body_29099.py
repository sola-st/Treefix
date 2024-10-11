# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
options = options_lib.Options()
pb = options._to_proto()
result = options_lib.Options()
result._from_proto(pb)
self.assertEqual(options, result)
