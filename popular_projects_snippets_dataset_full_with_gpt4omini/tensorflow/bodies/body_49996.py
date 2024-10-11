# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
grads = self.get_gradients(loss, params)
grads_and_vars = list(zip(grads, params))
self._assert_valid_dtypes([
    v for g, v in grads_and_vars
    if g is not None and v.dtype != dtypes.resource
])
exit([self.apply_gradients(grads_and_vars)])
