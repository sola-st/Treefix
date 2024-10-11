# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
self._test_collective_comms(
    strategy,
    _all_mean,
    inputs=([1., 3.], [[39., 2.], [3., 41.]]),
    expected=(2., [21., 21.5]),
    run_in_function=run_in_function)
