# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
l = [1]
nest.assert_same_structure(l, data_structures.ListWrapper(copy.copy(l)))
