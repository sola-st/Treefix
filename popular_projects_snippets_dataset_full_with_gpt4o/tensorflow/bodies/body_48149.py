# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Sets self.optimizer.

    Sets self.optimizer to `optimizer`, potentially wrapping it with a
    LossScaleOptimizer.

    Args:
      optimizer: The optimizer(s) to assign to self.optimizer.
    """
if isinstance(optimizer, (list, tuple)):
    self.optimizer = [optimizers.get(opt) for opt in optimizer]
else:
    self.optimizer = optimizers.get(optimizer)

if isinstance(self._dtype_policy, policy.PolicyV1):
    loss_scale = self._dtype_policy.loss_scale
elif self._dtype_policy.name == 'mixed_float16':
    loss_scale = 'dynamic'
else:
    loss_scale = None

if (loss_scale is not None and
    not isinstance(self.optimizer,
                   loss_scale_optimizer.LossScaleOptimizer)):
    if isinstance(self.optimizer, list):
        raise ValueError('When a dtype policy with a loss scale is used, you '
                         'can only pass a single optimizer. Using policy %s '
                         'and got optimizers: %s' %
                         self._dtype_policy, self.optimizer)
    if not isinstance(self.optimizer, optimizer_v2.OptimizerV2):
        raise ValueError('"optimizer" must be an instance of '
                         'tf.keras.optimizers.Optimizer when a dype policy '
                         'with a loss scale  used, but got: %s. Using policy: '
                         '%s' %
                         (self.optimizer, self._dtype_policy))
    if loss_scale == 'dynamic':
        self.optimizer = loss_scale_optimizer.LossScaleOptimizer(self.optimizer)
    else:
        self.optimizer = loss_scale_optimizer.LossScaleOptimizerV1(
            self.optimizer, loss_scale)
