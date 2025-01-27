# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Called in `apply_gradients` after aggregation."""
if self._clipvalue is not None:
    grads_and_vars = self._clipvalue_fn(grads_and_vars)
if self._clipnorm is not None:
    grads_and_vars = self._clipnorm_fn(grads_and_vars)
if self._global_clipnorm is not None:
    grads_and_vars = self._global_clipnorm_fn(grads_and_vars)

for fn in self.gradient_transformers:
    grads_and_vars = fn(grads_and_vars)
exit(grads_and_vars)
