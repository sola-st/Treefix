# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Writes `value` into index named by `index`.

    Args:
      index: 0-D.  int32 scalar with the index to write to.
      value: N-D.  Tensor of type `dtype`.  The `Tensor` to write to `index`.

    Raises:
      errors_impl.InvalidArgumentError: `value` dtype does not match dtype.
      errors_impl.OutOfRangeError: `index` is out of bounds.
      ValueError: shape of `value` is not consistent with inferred shape.
    """

if isinstance(index, ops.EagerTensor):
    index = index.numpy()

if index < 0:
    raise errors_impl.OutOfRangeError(
        None, None,
        "Writing to negative indices (index %d) is not allowed." % index)

size = len(self._tensor_array)
if index >= size:
    if not self._dynamic_size:
        raise errors_impl.OutOfRangeError(
            None, None,
            "Tried to write to index %d but array is not resizeable and size "
            "is: %d " % (index, size))
    self._tensor_array.extend(None for _ in range(index - size + 1))

if not isinstance(value, ops.EagerTensor):
    # TODO(b/129870929): Fix after all callers provide proper init dtype.
    value = ops.convert_to_tensor(
        value, preferred_dtype=self._dtype, name="value")

if self._dtype != value.dtype:
    raise errors_impl.InvalidArgumentError(
        None, None,
        "TensorArray dtype is %s but Op is trying to write dtype %s " %
        (self._dtype.name, value.dtype.name))

if not self._element_shape.is_compatible_with(value.shape):
    raise ValueError("Incompatible shape for value (%s), expected (%s)" %
                     (value.shape, self._element_shape))

if self._infer_shape:
    self._element_shape = self._element_shape.merge_with(value.shape)

self._tensor_array[index] = value
