# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
self._test_collective_comms_gradients(
    strategy, _all_mean, inputs=[1., 3.], expected_grads=[2., 2.],
    run_in_function=run_in_function)
