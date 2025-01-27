# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
# Collective ops doesn't support strategy with one device.
if context.executing_eagerly():
    strategy, _ = self._get_test_object(
        None, None, required_gpus, use_devices_arg=use_devices_arg)
    self._test_minimize_loss_eager(strategy)
else:
    self._test_minimize_loss_graph(None, None, required_gpus)
