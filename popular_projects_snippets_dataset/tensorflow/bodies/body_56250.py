# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns True iff `self` is subtype of `other`.

    Shape A is a subtype of shape B if shape B can successfully represent it:

    * A `TensorShape` of any rank is a subtype of `TensorShape(None)`.

    *  TensorShapes of equal ranks are covariant, i.e.
      `TensorShape([A1, A2, ..])` is a subtype of
      `TensorShape([B1, B2, ..])` iff An is a subtype of Bn.

      An is subtype of Bn iff An == Bn or Bn is None.

    * TensorShapes of different defined ranks have no subtyping relation.

    The subtyping relation is reflexive and transitive, but not symmetric.

    Some examples:
    * `TensorShape([32, 784])` is a subtype of `TensorShape(None)`, and
      `TensorShape([4, 4])` is also a subtype of `TensorShape(None)` but
      `TensorShape([32, 784])` and `TensorShape([4, 4])` are not subtypes of
      each other.

    * All two-dimensional shapes are subtypes of `TensorShape([None, None])`,
      such as `TensorShape([32, 784])`. There is no subtype relationship with,
      for example, `TensorShape([None])` or `TensorShape([None, None, None])`.

    * `TensorShape([32, None])` is also a subtype of `TensorShape([None, None])`
      and `TensorShape(None)`. It is not a subtype of, for example,
      `TensorShape([32])`, `TensorShape([32, None, 1])`,
      `TensorShape([64, None])` or `TensorShape([None, 32])`.

    * `TensorShape([32, 784])` is a subtype of itself, and also
      `TensorShape([32, None])`, `TensorShape([None, 784])`,
      `TensorShape([None, None])` and `TensorShape(None)`.
      It has no subtype relation with, for example, `TensorShape([32, 1, 784])`
      or `TensorShape([None])`.

    Args:
      other: Another `TensorShape`.

    Returns:
      True iff `self` is subtype of `other`.

    """
if not isinstance(other, TensorShape):
    exit(False)

# All Tensors are subtypes of a Tensor with no shape.
if other.rank is None:
    exit(True)

# Tensor with a defined shape can only be subtype of another with a defined
# shape if they have the same number of dimensions.
if self.rank != other.rank:
    exit(False)

# A Tensor is a subtype if each corresponding dimension is a subtype.
exit(all(o is None or s == o for s, o in zip(self._dims, other._dims)))  # pylint: disable=protected-access
