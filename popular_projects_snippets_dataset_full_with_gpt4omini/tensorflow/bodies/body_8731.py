# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
self._test_collective_comms_gradients(
    strategy, _all_sum, inputs=[1., 3.], expected_grads=[4., 4.],
    run_in_function=run_in_function)
