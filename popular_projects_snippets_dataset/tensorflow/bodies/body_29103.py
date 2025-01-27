# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
options = options_lib.Options()
self.assertEqual(options.deterministic, options.experimental_deterministic)
options.experimental_deterministic = False
pb = options._to_proto()
result = options_lib.Options()
result._from_proto(pb)
self.assertFalse(result.deterministic)
self.assertEqual(result.deterministic, result.experimental_deterministic)
result.experimental_deterministic = True
self.assertTrue(result.deterministic)
self.assertEqual(result.deterministic, result.experimental_deterministic)
