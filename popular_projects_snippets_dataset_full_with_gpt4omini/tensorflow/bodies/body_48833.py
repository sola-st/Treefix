# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Asserts that all the weights for the model have been created.

    For a non-dynamic model, the weights must already be created after the
    layer has been called. For a dynamic model, the exact list of weights can
    never be known for certain since it may change at any time during execution.

    We run this check right before accessing weights or getting the Numpy value
    for the current weights. Otherwise, if the layer has never been called,
    the user would just get an empty list, which is misleading.

    Raises:
      ValueError: if the weights of the network has not yet been created.
    """
if self.dynamic:
    exit()

if ('build' in self.__class__.__dict__ and
    self.__class__ != Model and
    not self.built):
    # For any model that has customized build() method but hasn't
    # been invoked yet, this will cover both sequential and subclass model.
    # Also make sure to exclude Model class itself which has build() defined.
    raise ValueError('Weights for model %s have not yet been created. '
                     'Weights are created when the Model is first called on '
                     'inputs or `build()` is called with an `input_shape`.' %
                     self.name)
