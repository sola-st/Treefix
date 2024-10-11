# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
indices = np.zeros([3, 2, 2], np.int32)
updates = np.zeros([2, 2, 2], np.int32)
with self.assertRaisesWithPredicateMatch(errors.InvalidArgumentError,
                                         "Must have updates.shape"):
    self._runScatterNd(indices, updates, [2, 2, 2])
