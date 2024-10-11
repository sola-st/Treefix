# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
super(Adadelta, self).__init__(**kwargs)
with backend.name_scope(self.__class__.__name__):
    self.lr = backend.variable(lr, name='lr')
    self.decay = backend.variable(decay, name='decay')
    self.iterations = backend.variable(0, dtype='int64', name='iterations')
if epsilon is None:
    epsilon = backend.epsilon()
self.rho = rho
self.epsilon = epsilon
self.initial_decay = decay
