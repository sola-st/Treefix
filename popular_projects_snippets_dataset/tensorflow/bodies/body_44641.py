# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/logical_test.py
self.assertFalse(logical.not_(True))
self.assertFalse(logical.not_([1]))
self.assertTrue(logical.not_([]))
