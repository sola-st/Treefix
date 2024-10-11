# Extracted from ./data/repos/tensorflow/tensorflow/python/training/rmsprop.py
lr = self._call_if_callable(self._learning_rate)
decay = self._call_if_callable(self._decay)
momentum = self._call_if_callable(self._momentum)
epsilon = self._call_if_callable(self._epsilon)

self._learning_rate_tensor = ops.convert_to_tensor(lr, name="learning_rate")
self._decay_tensor = ops.convert_to_tensor(decay, name="decay")
self._momentum_tensor = ops.convert_to_tensor(momentum, name="momentum")
self._epsilon_tensor = ops.convert_to_tensor(epsilon, name="epsilon")
