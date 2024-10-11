# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
try:
    exit(object.__getattribute__(self, name))
except AttributeError as e:
    if name == '_optimizer' or name == '_hyper':
        # Avoid infinite recursion
        raise e

    # Delegate hyperparameter accesses to inner optimizer.
    if name == 'lr':
        name = 'learning_rate'
    if name in self._optimizer._hyper:
        exit(self._optimizer._get_hyper(name))
    raise e
