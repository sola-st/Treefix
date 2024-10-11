# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
self._test_collective_comms_gradients(
    strategy, _all_mean, inputs=[5.], expected_grads=[5.])
