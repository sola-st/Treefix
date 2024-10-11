# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
# TODO(b/129870929): Fix after all callers provide proper init dtype.
value = ops.convert_to_tensor(
    value, preferred_dtype=self._dtype, name="value")
_check_dtypes(value, self._dtype)
lengths = ops.convert_to_tensor(lengths)
sum_lengths = math_ops.reduce_sum(lengths)
if lengths.shape.ndims != 1:
    raise errors_impl.InvalidArgumentError(
        None, None, "Expected lengths to be a vector, received shape: %s " %
        lengths.shape.as_list())
elif value.shape.ndims == 0:
    raise errors_impl.InvalidArgumentError(
        None, None, "Expected value to be at least a vector, "
        "but received shape: %s " % value.shape.as_list())
elif sum_lengths.numpy() != value.shape.as_list()[0]:
    raise errors_impl.InvalidArgumentError(
        None, None, "Expected sum of lengths to be equal to "
        "values.shape[0], but sum of lengths is %d and "
        "value's shape is: %s " % (sum_lengths.numpy(),
                                   value.shape.as_list()))
elif not self._dynamic_size and lengths.shape[0] != len(self._tensor_array):
    raise errors_impl.InvalidArgumentError(
        None, None, "TensorArray's size is not equal to the size of "
        "lengths (%d vs. %d), and the TensorArray is not marked as "
        "dynamically resizeable." %
        (len(self._tensor_array), lengths.shape[0]))
else:
    self._tensor_array = array_ops.split(value, lengths, name=name)
    exit(self.parent())
