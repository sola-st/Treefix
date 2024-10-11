# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py

def get_factory(use_time_major):

    def factory(scope):
        exit(self._createBidirectionalDynamicRNN(
            use_shape=True,
            use_state_tuple=True,
            use_sequence_length=True,
            use_time_major=use_time_major,
            scope=scope))

    exit(factory)

self._testScope(get_factory(True), use_outer_scope=True)
self._testScope(get_factory(True), use_outer_scope=False)
self._testScope(get_factory(True), prefix=None, use_outer_scope=False)
self._testScope(get_factory(False), use_outer_scope=True)
self._testScope(get_factory(False), use_outer_scope=False)
self._testScope(get_factory(False), prefix=None, use_outer_scope=False)
