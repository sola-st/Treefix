# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
structure = np.array([1, 2, 3])
flattened = nest.flatten(structure)
self.assertLen(flattened, 1)
