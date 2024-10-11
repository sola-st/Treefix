# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy()
self._test_all_reduce_sum_gradient_tape(strategy, run_in_function=True)
