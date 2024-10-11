# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
# Tests that execute collectives need to be enclosed in graph or tf.function
with ops.Graph().as_default():
    self._testCollectiveBroadcast([0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1])
