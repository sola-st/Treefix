# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
l = data_structures._TupleWrapper((1,))
l *= 0
self.assertEqual((), l)
