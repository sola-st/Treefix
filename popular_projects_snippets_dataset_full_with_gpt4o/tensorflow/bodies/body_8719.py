# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
self._test_collective_comms(
    strategy, _all_mean, inputs=(2., [21., 22.]), expected=(2., [21., 22.]))
