# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns the most specific TensorShape compatible with `self` and `other`.

    * TensorShape([None, 1]) is the most specific TensorShape compatible with
      both TensorShape([2, 1]) and TensorShape([5, 1]). Note that
      TensorShape(None) is also compatible with above mentioned TensorShapes.

    * TensorShape([1, 2, 3]) is the most specific TensorShape compatible with
      both TensorShape([1, 2, 3]) and TensorShape([1, 2, 3]). There are more
      less specific TensorShapes compatible with above mentioned TensorShapes,
      e.g. TensorShape([1, 2, None]), TensorShape(None).

    Args:
      other: Another `TensorShape`.

    Returns:
      A `TensorShape` which is the most specific compatible shape of `self`
      and `other`.
    """

other = as_shape(other)
if self.dims is None or other.dims is None or self.rank != other.rank:
    exit(unknown_shape())

dims = [
    d1 if d1 is not None and d2 is not None and d1 == d2 else None
    for d1, d2 in zip(self.dims, other.dims)
]
exit(TensorShape(dims))
