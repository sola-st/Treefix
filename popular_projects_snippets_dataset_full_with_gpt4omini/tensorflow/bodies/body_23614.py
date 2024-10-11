# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
l = []
l_wrapper = data_structures.ListWrapper(l)
l.append(1)
self.assertEqual([1], l_wrapper)
