# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v1.py
self.optimizer = optimizer
self._track_trackable(optimizer, name='optimizer')
if iterations is None:
    with backend.name_scope(self.__class__.__name__):
        self.iterations = backend.variable(0, dtype='int64', name='iterations')
else:
    self.iterations = iterations
self._track_trackable(self.iterations, name='global_step')
