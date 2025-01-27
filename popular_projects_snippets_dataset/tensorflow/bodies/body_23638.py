# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
self.assertEqual([1., 2.],
                 data_structures.ListWrapper([1.])
                 + data_structures.ListWrapper([2.]))
self.assertEqual([1., 2.],
                 data_structures.ListWrapper([1.])
                 + [2.])
self.assertEqual([1., 2.],
                 [1.]
                 + data_structures.ListWrapper([2.]))
