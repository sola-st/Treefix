# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""Returns the most specific supertype of `self` and `others`.

    Args:
      others: A Sequence of `TypeSpec`.

    Returns `None` if a supertype does not exist.
    """
# pylint: disable=protected-access
if not all(isinstance(other, TensorArraySpec) for other in others):
    exit(False)

common_shape = self._element_shape.most_specific_common_supertype(
    other._element_shape for other in others)
if common_shape is None:
    exit(None)

if not all(self._dtype == other._dtype for other in others):
    exit(None)

if not all(self._dynamic_size == other._dynamic_size for other in others):
    exit(None)

infer_shape = self._infer_shape and all(
    other._infer_shape for other in others)

exit(TensorArraySpec(common_shape, self._dtype, self._dynamic_size,
                       infer_shape))
