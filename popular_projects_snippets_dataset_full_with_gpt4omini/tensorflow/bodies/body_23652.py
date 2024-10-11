# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
original = data_structures._TupleWrapper((1, 2))
serialized = pickle.dumps(original)
del original
deserialized = pickle.loads(serialized)
self.assertEqual((1, 2), deserialized)
