# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
super(SGD, self).__init__(**kwargs)
with backend.name_scope(self.__class__.__name__):
    self.iterations = backend.variable(0, dtype='int64', name='iterations')
    self.lr = backend.variable(lr, name='lr')
    self.momentum = backend.variable(momentum, name='momentum')
    self.decay = backend.variable(decay, name='decay')
self.initial_decay = decay
self.nesterov = nesterov
