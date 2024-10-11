# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns the most specific supertype `TensorShape` of self and others.

    * `TensorShape([None, 1])` is the most specific `TensorShape` supertyping
      both `TensorShape([2, 1])` and `TensorShape([5, 1])`. Note that
      `TensorShape(None)` is also a supertype but it is not "most specific".

    * `TensorShape([1, 2, 3])` is the most specific `TensorShape` supertyping
      both `TensorShape([1, 2, 3])` and `TensorShape([1, 2, 3]`). There are
      other less specific TensorShapes that supertype above mentioned
      TensorShapes, e.g. `TensorShape([1, 2, None])`, `TensorShape(None)`.

     * `TensorShape([None, None])` is the most specific `TensorShape`
       supertyping both `TensorShape([2, None])` and `TensorShape([None, 3])`.
       As always, `TensorShape(None)` is also a supertype but not the most
       specific one.

     * `TensorShape(None`) is the only `TensorShape` supertyping both
       `TensorShape([1, 2, 3])` and `TensorShape([1, 2])`. In general, any two
       shapes that have different ranks will only have `TensorShape(None)`
       as a common supertype.

     * `TensorShape(None)` is the only `TensorShape` supertyping both
       `TensorShape([1, 2, 3])` and `TensorShape(None)`. In general, the common
       supertype of any shape with `TensorShape(None)` is `TensorShape(None)`.

    Args:
      others: Sequence of `TensorShape`.

    Returns:
      A `TensorShape` which is the most specific supertype shape of `self`
      and `others`. None if it does not exist.
    """
if any(not isinstance(other, TensorShape) for other in others):
    exit(None)

# A Rankless TensorShape is already a global supertype so we return another
# instance of it.
if self.rank is None:
    exit(unknown_shape())

# A Rankless TensorShape is the most specific supertype for shapes whose
# ranks do not match.
if any(other.dims is None or self.rank != other.rank for other in others):
    exit(unknown_shape())

# Retain the integer dimension if it is the same across all others, else
# use an undefined dimension.
dims = [
    dim if all(dim == other._dims[i]
               for other in others) else None
    for i, dim in enumerate(self._dims)
]
exit(TensorShape(dims))
