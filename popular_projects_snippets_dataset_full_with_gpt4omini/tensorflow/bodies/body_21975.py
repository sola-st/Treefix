# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam.py
lr = self._call_if_callable(self._lr)
beta1 = self._call_if_callable(self._beta1)
beta2 = self._call_if_callable(self._beta2)
epsilon = self._call_if_callable(self._epsilon)

self._lr_t = ops.convert_to_tensor(lr, name="learning_rate")
self._beta1_t = ops.convert_to_tensor(beta1, name="beta1")
self._beta2_t = ops.convert_to_tensor(beta2, name="beta2")
self._epsilon_t = ops.convert_to_tensor(epsilon, name="epsilon")
