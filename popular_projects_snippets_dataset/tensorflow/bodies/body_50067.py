# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adam.py
super(Adam, self).__init__(name, **kwargs)
self._set_hyper('learning_rate', kwargs.get('lr', learning_rate))
self._set_hyper('decay', self._initial_decay)
self._set_hyper('beta_1', beta_1)
self._set_hyper('beta_2', beta_2)
self.epsilon = epsilon or backend_config.epsilon()
self.amsgrad = amsgrad
