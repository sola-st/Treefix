# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/gradient_descent.py
super(SGD, self).__init__(name, **kwargs)
self._set_hyper("learning_rate", kwargs.get("lr", learning_rate))
self._set_hyper("decay", self._initial_decay)

self._momentum = False
if isinstance(momentum, ops.Tensor) or callable(momentum) or momentum > 0:
    self._momentum = True
if isinstance(momentum, (int, float)) and (momentum < 0 or momentum > 1):
    raise ValueError("`momentum` must be between [0, 1].")
self._set_hyper("momentum", momentum)

self.nesterov = nesterov
