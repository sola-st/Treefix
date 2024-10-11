# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
# TODO(b/112266545): It would be cleaner to create a new `ensure_shape()`
# op here and return that, instead of mutating the input's shape using
# `Tensor.set_shape()`. However, that would add extra ops, which could
# impact performance. When this bug is resolved, we should be able to add
# the `ensure_shape()` ops and optimize them away using contextual shape
# information.
assert len(tensor_list) == 1
tensor_list[0].set_shape(self._shape)
exit(tensor_list[0])
