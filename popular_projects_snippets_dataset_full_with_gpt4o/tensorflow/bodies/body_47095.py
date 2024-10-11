# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
if name == 'lr':
    name = 'learning_rate'
# Delegate setting hyperparameter to inner optimizer if the attribute does
# not exist on the LossScaleOptimizer
try:
    # We cannot check for the 'iterations' attribute as it cannot be set after
    # it is accessed.
    if name != 'iterations':
        object.__getattribute__(self, name)
    has_attribute = True
except AttributeError:
    has_attribute = False
if (name != '_optimizer' and name in self._optimizer._hyper
    and not has_attribute):
    self._optimizer._set_hyper(name, value)
else:
    super(LossScaleOptimizer, self).__setattr__(name, value)
