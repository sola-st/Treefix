# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/logical_test.py
self.assertFalse(logical.or_(lambda: False, lambda: False))
self.assertFalse(logical.or_(lambda: [], lambda: False))
self.assertListEqual(logical.or_(lambda: False, lambda: [1]), [1])

self.assertTrue(logical.or_(lambda: False, lambda: True))
self.assertTrue(logical.or_(lambda: True, self.assertNotCalled))
