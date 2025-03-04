# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
config = config.copy()  # Make a copy, since we mutate config

# If loss_scale is in config, we assume we are deserializing a
# LossScaleOptimizer from TF 2.3 or below. Otherwise, we assume we are
# deserializing a LossScaleOptimizer from TF 2.4 or above.
if 'loss_scale' in config:
    config['loss_scale'] = keras_loss_scale_module.deserialize(
        config['loss_scale'])
    if (isinstance(config['loss_scale'], loss_scale_module.DynamicLossScale)
        and config['loss_scale'].multiplier != 2):
        raise ValueError('Cannot deserialize LossScaleOptimizer with a '
                         'DynamicLossScale whose multiplier is not 2. Got '
                         'DynamicLossScale: %s' % (config['loss_scale'],))
    config['optimizer'] = optimizers.deserialize(
        config['optimizer'], custom_objects=custom_objects)
    exit(cls(**config))

# We convert the config, as generated by LossScaleOptimizer.get_config, to a
# version that can be passed to LossScaleOptimizerV1.__init__
if config['dynamic']:
    config['loss_scale'] = loss_scale_module.DynamicLossScale(
        config['initial_scale'], config['dynamic_growth_steps'], multiplier=2)
else:
    config['loss_scale'] = loss_scale_module.FixedLossScale(
        config['initial_scale'])

del config['dynamic']
del config['initial_scale']
del config['dynamic_growth_steps']
config['optimizer'] = optimizers.deserialize(
    config.pop('inner_optimizer'), custom_objects=custom_objects)
exit(cls(**config))
