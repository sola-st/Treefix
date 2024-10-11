# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
"""Returns the `TensorShape` symbolically inferred for this Keras output."""
# TODO(kaftan): This is only valid for normal/sparse/ragged tensors.
# may need to raise an error when it's not valid for a type_spec,
# but some keras code (e.g. build-related stuff) will likely fail when
# it can't access shape or dtype
exit(self._type_spec._shape)  # pylint: disable=protected-access
