# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
if not isinstance(inner_optimizer, optimizer_v2.OptimizerV2):
    raise TypeError('"inner_optimizer" must be an instance of OptimizerV2, '
                    'but got: %s' % inner_optimizer)
if not isinstance(dynamic, bool):
    # Catch errors if a user incorrectly passes a string or float to the
    # second argument argument, as this is commonly done for
    # LossScaleOptimizerV1.
    raise TypeError('"dynamic" argument to LossScaleOptimizer.__init__ must '
                    'be a bool, but got: %r' % (dynamic,))
if isinstance(inner_optimizer, LossScaleOptimizer):
    raise TypeError('LossScaleOptimizer cannot wrap another '
                    'LossScaleOptimizer, but got: %s' % (inner_optimizer,))
self._raise_if_strategy_unsupported()
if getattr(inner_optimizer, '_is_wrapped_by_loss_scale_optimizer', False):
    # TODO(reedwm): Maybe support this. The difficulty is that LSO has the
    # same checkpoint format as the inner optimizer, so multiple LSOs wrapping
    # the same optimizer causes the checkpointing logic to become confused.
    raise ValueError('"inner_optimizer" is already wrapped by a '
                     'LossScaleOptimizer. An optimizer can only be wrapped '
                     'by a single LossScaleOptimizer')
self._optimizer = inner_optimizer
self._optimizer._is_wrapped_by_loss_scale_optimizer = True

# We don't call super().__init__, since we do not want to call OptimizerV2's
# constructor.
base_delegate.DelegatingTrackableMixin.__init__(self, self._optimizer)

if dynamic:
    if initial_scale is None:
        initial_scale = _DEFAULT_INITIAL_SCALE
    if dynamic_growth_steps is None:
        dynamic_growth_steps = _DEFAULT_GROWTH_STEPS
    self._loss_scale = _DynamicLossScaleState(
        initial_scale, dynamic_growth_steps, multiplier=2)
    self._track_trackable(self._loss_scale, 'loss_scale')
else:
    if initial_scale is None:
        raise ValueError('"initial_scale" must be specified if "dynamic" is '
                         'False')
    self._loss_scale = float(initial_scale)
    if dynamic_growth_steps is not None:
        raise ValueError('"dynamic_growth_steps" must be None if "dynamic" '
                         'is False, but got: %s' % (dynamic_growth_steps,))

    # To support restoring TensorFlow 2.2 checkpoints.
self._track_trackable(FakeOptimizerForRestoration(self._optimizer),
                      'base_optimizer')
