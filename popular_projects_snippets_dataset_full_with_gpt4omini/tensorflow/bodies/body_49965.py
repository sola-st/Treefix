# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adagrad.py
if initial_accumulator_value < 0.0:
    raise ValueError('initial_accumulator_value must be non-negative: %s' %
                     initial_accumulator_value)
if epsilon is None:
    epsilon = backend_config.epsilon()
super(Adagrad, self).__init__(name, **kwargs)
self._set_hyper('learning_rate', kwargs.get('lr', learning_rate))
self._set_hyper('decay', self._initial_decay)
self._initial_accumulator_value = initial_accumulator_value
self.epsilon = epsilon or backend_config.epsilon()
