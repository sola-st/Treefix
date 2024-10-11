# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
# Checks whether `compile` has been called. If it has been called,
# then the optimizer is set. This is different from whether the
# model is compiled
# (i.e. whether the model is built and its inputs/outputs are set).
if not self._compile_was_called:
    raise RuntimeError('You must compile your model before '
                       'training/testing. '
                       'Use `model.compile(optimizer, loss)`.')
