# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
warn_msg_prefix = (
    'tf.keras.mixed_precision.experimental.LossScaleOptimizer is '
    'deprecated. Please use tf.keras.mixed_precision.LossScaleOptimizer '
    'instead. ')

if isinstance(loss_scale, dict):
    loss_scale = keras_loss_scale_module.deserialize(loss_scale)

if isinstance(loss_scale, (int, float)):
    tf_logging.warning(
        warn_msg_prefix + 'For example:\n'
        '  opt = tf.keras.mixed_precision.LossScaleOptimizer('
        'opt, dynamic=False, initial_scale={})'.format(loss_scale))
    super(LossScaleOptimizerV1, self).__init__(optimizer, dynamic=False,
                                               initial_scale=loss_scale)
elif isinstance(loss_scale, loss_scale_module.FixedLossScale):
    ls_val = loss_scale._loss_scale_value  # pylint: disable=protected-access
    tf_logging.warning(
        warn_msg_prefix + 'For example:\n'
        '  opt = tf.keras.mixed_precision.LossScaleOptimizer('
        'opt, dynamic=False, initial_scale={})'.format(ls_val))
    super(LossScaleOptimizerV1, self).__init__(optimizer, dynamic=False,
                                               initial_scale=ls_val)
elif loss_scale == 'dynamic':
    tf_logging.warning(
        warn_msg_prefix + 'For example:\n'
        '  opt = tf.keras.mixed_precision.LossScaleOptimizer('
        'opt)')
    super(LossScaleOptimizerV1, self).__init__(optimizer)
elif isinstance(loss_scale, loss_scale_module.DynamicLossScale):
    kwargs = {}
    extra_arguments = ''
    if loss_scale.initial_loss_scale != _DEFAULT_INITIAL_SCALE:
        kwargs['initial_scale'] = loss_scale.initial_loss_scale
        extra_arguments += (', initial_scale=%s' %
                            loss_scale.initial_loss_scale)
    if loss_scale.increment_period != _DEFAULT_GROWTH_STEPS:
        kwargs['dynamic_growth_steps'] = loss_scale.increment_period
        extra_arguments += (', dynamic_growth_steps=%s' %
                            loss_scale.increment_period)
    if loss_scale.multiplier != 2:
        raise ValueError('When passing a DynamicLossScale to "loss_scale", '
                         'DynamicLossScale.multiplier must be 2. Got: %s'
                         % (loss_scale,))
    tf_logging.warning(
        warn_msg_prefix +
        'Note that the non-experimental LossScaleOptimizer does not take a '
        'DynamicLossScale but instead takes the dynamic configuration '
        'directly in the constructor. For example:\n'
        '  opt = tf.keras.mixed_precision.LossScaleOptimizer('
        'opt{})\n'.format(extra_arguments))
    super(LossScaleOptimizerV1, self).__init__(optimizer, **kwargs)
elif isinstance(loss_scale, loss_scale_module.LossScale):
    raise TypeError('Passing a LossScale that is not a FixedLossScale or a '
                    'DynamicLossScale is no longer supported. Got: {}'
                    .format(loss_scale))
else:
    raise ValueError('Invalid value passed to loss_scale. loss_scale '
                     'must be the string "dynamic" (recommended), an int, '
                     'a float, a FixedLossScale, or a DynamicLossScale. Got '
                     'value: {}'.format(loss_scale))
