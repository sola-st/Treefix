# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
if val is not None and self.gradient_transformers:
    raise ValueError("`clipvalue` cannot be set when `gradient_transformers` "
                     "is set. Instead, use the `gradient_transformers` to "
                     "specify clipping and other transformations.")
self._clipvalue = val
self._clipvalue_fn = optimizer_utils.make_gradient_clipvalue_fn(
    self._clipvalue)
