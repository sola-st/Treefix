# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adadelta.py
super(Adadelta, self).__init__(name, **kwargs)
self._set_hyper('learning_rate', kwargs.get('lr', learning_rate))
self._set_hyper('decay', self._initial_decay)
self._set_hyper('rho', rho)
self.epsilon = epsilon or backend_config.epsilon()
