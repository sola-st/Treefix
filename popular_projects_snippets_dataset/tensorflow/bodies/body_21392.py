# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum.py
learning_rate = self._learning_rate
if callable(learning_rate):
    learning_rate = learning_rate()
self._learning_rate_tensor = ops.convert_to_tensor(learning_rate,
                                                   name="learning_rate")
momentum = self._momentum
if callable(momentum):
    momentum = momentum()
self._momentum_tensor = ops.convert_to_tensor(momentum, name="momentum")
