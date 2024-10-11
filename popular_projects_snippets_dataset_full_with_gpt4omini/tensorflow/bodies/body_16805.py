# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
# Tests that execute collectives need to be enclosed in graph or tf.function
with ops.Graph().as_default():
    self._testCollectiveGather([0, 1, 2, 3, 4, 5, 6, 7],
                               [10, 11, 12, 13, 14, 15, 16, 17],
                               [0, 1, 2, 3, 4, 5, 6, 7,
                                10, 11, 12, 13, 14, 15, 16, 17],
                               True)
    self._testCollectiveGather([[0, 1, 2, 3], [4, 5, 6, 7]],
                               [[10, 11, 12, 13], [14, 15, 16, 17]],
                               [[0, 1, 2, 3], [4, 5, 6, 7],
                                [10, 11, 12, 13], [14, 15, 16, 17]],
                               True)
    self._testCollectiveGather([[[0, 1], [2, 3]], [[4, 5], [6, 7]]],
                               [[[10, 11], [12, 13]], [[14, 15], [16, 17]]],
                               [[[0, 1], [2, 3]], [[4, 5], [6, 7]],
                                [[10, 11], [12, 13]], [[14, 15], [16, 17]]],
                               True)
