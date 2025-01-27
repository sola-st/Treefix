# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py

def factory(scope):
    exit(self._createBidirectionalRNN(
        use_shape=True, use_sequence_length=True, scope=scope))

self._testScope(factory, use_outer_scope=True)
self._testScope(factory, use_outer_scope=False)
self._testScope(factory, prefix=None, use_outer_scope=False)
