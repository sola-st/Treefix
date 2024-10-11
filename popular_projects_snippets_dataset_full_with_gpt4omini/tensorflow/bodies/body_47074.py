# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
if not strategy_supports_loss_scaling():
    strategy = distribution_strategy_context.get_strategy()
    if isinstance(strategy,
                  (tpu_strategy.TPUStrategy, tpu_strategy.TPUStrategyV1,
                   tpu_strategy.TPUStrategyV2)):
        raise ValueError(
            'Loss scaling is not supported with TPUStrategy. Loss scaling is '
            'unnecessary with TPUs, since they support bfloat16 instead of '
            'float16 and bfloat16 does not require loss scaling. You should '
            'remove the use of the LossScaleOptimizer when TPUs are used.')
    else:
        raise ValueError('Loss scaling is not supported with the '
                         'tf.distribute.Strategy: %s. Try using a different '
                         'Strategy, e.g. a MirroredStrategy' %
                         strategy.__class__.__name__)
