# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/ftrl.py
super(Ftrl, self).__init__(name, **kwargs)

if initial_accumulator_value < 0.0:
    raise ValueError(
        'initial_accumulator_value %f needs to be positive or zero' %
        initial_accumulator_value)
if learning_rate_power > 0.0:
    raise ValueError('learning_rate_power %f needs to be negative or zero' %
                     learning_rate_power)
if l1_regularization_strength < 0.0:
    raise ValueError(
        'l1_regularization_strength %f needs to be positive or zero' %
        l1_regularization_strength)
if l2_regularization_strength < 0.0:
    raise ValueError(
        'l2_regularization_strength %f needs to be positive or zero' %
        l2_regularization_strength)
if l2_shrinkage_regularization_strength < 0.0:
    raise ValueError(
        'l2_shrinkage_regularization_strength %f needs to be positive'
        ' or zero' % l2_shrinkage_regularization_strength)

self._set_hyper('learning_rate', learning_rate)
self._set_hyper('decay', self._initial_decay)
self._set_hyper('learning_rate_power', learning_rate_power)
self._set_hyper('l1_regularization_strength', l1_regularization_strength)
self._set_hyper('l2_regularization_strength', l2_regularization_strength)
self._set_hyper('beta', beta)
self._initial_accumulator_value = initial_accumulator_value
self._l2_shrinkage_regularization_strength = (
    l2_shrinkage_regularization_strength)
