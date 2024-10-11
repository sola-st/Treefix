# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
cache = context._EagerTensorCache(max_items=100, max_tensor_size=3)
cache.put('1', array_ops.zeros((2, 2)))
self.assertIsNone(cache.get('1'))

cache.put('2', array_ops.zeros((2)))
self.assertIsNotNone(cache.get('2'))
