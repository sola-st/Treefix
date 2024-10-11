# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
result = data_structures._DictWrapper([(1, 2), (3, 4)])
self.assertIsInstance(result, dict)
self.assertEqual({1: 2, 3: 4}, result)
