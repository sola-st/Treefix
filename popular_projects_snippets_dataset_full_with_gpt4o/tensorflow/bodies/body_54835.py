# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
# pylint: disable=g-generic-assert
self.assertEqual(v1, v2)
self.assertEqual(v2, v1)
self.assertFalse(v1 != v2)
self.assertFalse(v2 != v1)
self.assertEqual(hash(v1), hash(v2))
