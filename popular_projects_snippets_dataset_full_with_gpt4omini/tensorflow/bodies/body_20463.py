# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
if not distribution_strategy_context.has_strategy():
    exit(None)
strategy = distribution_strategy_context.get_strategy()
if not is_tpu_strategy(strategy):
    exit(None)
exit(strategy.extended._device_assignment)  # pylint: disable=protected-access
