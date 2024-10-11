# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
if val is not None and self.gradient_transformers:
    raise ValueError("`clipnorm` cannot be set when `gradient_transformers` "
                     "is set. Instead, use the `gradient_transformers` to "
                     "specify clipping and other transformations.")
self._clipnorm = val
self._clipnorm_fn = optimizer_utils.make_gradient_clipnorm_fn(
    self._clipnorm)
