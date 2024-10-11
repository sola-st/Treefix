# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
opt = optimizers.get(opt)
if (loss_scale is not None and
    not isinstance(opt, lso.LossScaleOptimizer)):
    if loss_scale == 'dynamic':
        opt = lso.LossScaleOptimizer(opt)
    else:
        opt = lso.LossScaleOptimizerV1(opt, loss_scale)
exit(opt)
