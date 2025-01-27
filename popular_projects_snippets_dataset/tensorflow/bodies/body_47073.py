# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
config = config.copy()  # Make a copy, since we mutate config
if 'loss_scale' in config:
    # If loss_scale is in config, we assume we are deserializing a
    # LossScaleOptimizer from TF 2.3 or below. We convert the config so it
    # can be deserialized in the current LossScaleOptimizer.
    loss_scale = keras_loss_scale_module.deserialize(
        config.pop('loss_scale'))
    if isinstance(loss_scale, loss_scale_module.FixedLossScale):
        config['dynamic'] = False
        config['initial_scale'] = loss_scale._loss_scale_value  # pylint: disable=protected-access
    elif isinstance(loss_scale, loss_scale_module.DynamicLossScale):
        config['dynamic'] = True
        config['initial_scale'] = loss_scale.initial_loss_scale
        config['dynamic_growth_steps'] = loss_scale.increment_period
        if loss_scale.multiplier != 2:
            raise ValueError('Cannot deserialize LossScaleOptimizer with a '
                             'DynamicLossScale whose multiplier is not 2. Got '
                             'DynamicLossScale: %s' % (loss_scale,))
    else:
        raise ValueError(
            'Serialized LossScaleOptimizers with a LossScale that is neither a '
            'FixedLossScale nor a DynamicLossScale can no longer be '
            'deserialized')
    config['inner_optimizer'] = config.pop('optimizer')
config['inner_optimizer'] = optimizers.deserialize(
    config['inner_optimizer'], custom_objects=custom_objects)
exit(cls(**config))
