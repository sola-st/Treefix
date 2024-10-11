# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
original = data_structures._DictWrapper(dict(a=1, b=2))
serialized = pickle.dumps(original)
del original
deserialized = pickle.loads(serialized)
self.assertEqual(dict(a=1, b=2), deserialized)
