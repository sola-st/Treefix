# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
# Checks whether `compile` has been called. If it has been called,
# then the optimizer is set. This is different from whether the
# model is compiled
# (i.e. whether the model is built and its inputs/outputs are set).
if not self._is_compiled:
    raise RuntimeError('You must compile your model before '
                       'training/testing. '
                       'Use `model.compile(optimizer, loss)`.')
