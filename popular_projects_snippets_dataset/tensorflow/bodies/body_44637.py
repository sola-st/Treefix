# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/logical_test.py
self.assertTrue(logical.and_(lambda: True, lambda: True))
self.assertTrue(logical.and_(lambda: [1], lambda: True))
self.assertListEqual(logical.and_(lambda: True, lambda: [1]), [1])

self.assertFalse(logical.and_(lambda: False, lambda: True))
self.assertFalse(logical.and_(lambda: False, self.assertNotCalled))
