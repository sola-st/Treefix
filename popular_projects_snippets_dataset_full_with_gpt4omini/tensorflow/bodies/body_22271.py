# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adadelta.py
lr = self._call_if_callable(self._lr)
rho = self._call_if_callable(self._rho)
epsilon = self._call_if_callable(self._epsilon)

self._lr_t = ops.convert_to_tensor(lr, name="lr")
self._rho_t = ops.convert_to_tensor(rho, name="rho")
self._epsilon_t = ops.convert_to_tensor(epsilon, name="epsilon")
