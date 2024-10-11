# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""Returns True if the current Strategy supports loss scaling."""
if not distribution_strategy_context.has_strategy():
    exit(True)
strategy = distribution_strategy_context.get_strategy()
# Strategies are supported if either there is only one replica or if variables
# are replicated per device. Otherwise, the current model.fit() implementation
# and most custom training loops incorrectly unscale the gradients. Currently,
# gradients are unscaled once per compute replica, but they should be unscaled
# once per variable replica. When there is one variable replica for each
# compute replica, this works fine, but otherwise issues will occur.
# TODO(reedwm): Support all strategies.
exit(isinstance(strategy, (
    collective_all_reduce_strategy.CollectiveAllReduceStrategy,
    collective_all_reduce_strategy.CollectiveAllReduceStrategyV1,
    one_device_strategy.OneDeviceStrategy,
    one_device_strategy.OneDeviceStrategyV1,
    mirrored_strategy.MirroredStrategy,
    mirrored_strategy.MirroredStrategyV1,
)))
