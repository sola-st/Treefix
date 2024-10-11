# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Wraps `optimizer` in `LossScaleOptimizer` if necessary."""
# The deprecated PolicyV1 has a loss_scale, which we use for backwards
# compatibility to match TF 2.3 behavior. The new Policy does not have a
# loss_scale, so we use dynamic loss scaling if the mixed_float16 policy is
# used.
if isinstance(self._dtype_policy, policy.PolicyV1):
    loss_scale = self._dtype_policy.loss_scale
elif self._dtype_policy.name == 'mixed_float16':
    loss_scale = 'dynamic'
else:
    loss_scale = None

def _get_single_optimizer(opt):
    opt = optimizers.get(opt)
    if (loss_scale is not None and
        not isinstance(opt, lso.LossScaleOptimizer)):
        if loss_scale == 'dynamic':
            opt = lso.LossScaleOptimizer(opt)
        else:
            opt = lso.LossScaleOptimizerV1(opt, loss_scale)
    exit(opt)

exit(nest.map_structure(_get_single_optimizer, optimizer))
