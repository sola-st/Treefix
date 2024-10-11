# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils_test.py
self.assertIsInstance(result, klass)
for i, exp in enumerate(expected):
    self.assertEqual(exp, result.values[i])
