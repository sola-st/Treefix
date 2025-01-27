# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns True if `self` is equivalent to `other`.

    It first tries to convert `other` to `TensorShape`. `TypeError` is thrown
    when the conversion fails. Otherwise, it compares each element in the
    TensorShape dimensions.

    * Two *Fully known* shapes, return True iff each element is equal.
    >>> t_a = tf.TensorShape([1,2])
    >>> a = [1, 2]
    >>> t_b = tf.TensorShape([1,2])
    >>> t_c = tf.TensorShape([1,2,3])
    >>> t_a.__eq__(a)
    True
    >>> t_a.__eq__(t_b)
    True
    >>> t_a.__eq__(t_c)
    False

    * Two *Partially-known* shapes, return True iff each element is equal.
    >>> p_a = tf.TensorShape([1,None])
    >>> p_b = tf.TensorShape([1,None])
    >>> p_c = tf.TensorShape([2,None])
    >>> p_a.__eq__(p_b)
    True
    >>> t_a.__eq__(p_a)
    False
    >>> p_a.__eq__(p_c)
    False

    * Two *Unknown shape*, return True.
    >>> unk_a = tf.TensorShape(None)
    >>> unk_b = tf.TensorShape(None)
    >>> unk_a.__eq__(unk_b)
    True
    >>> unk_a.__eq__(t_a)
    False

    Args:
      other: A `TensorShape` or type that can be converted to `TensorShape`.

    Returns:
      True if the dimensions are all equal.

    Raises:
      TypeError if `other` can not be converted to `TensorShape`.
    """

try:
    other = as_shape(other)
except TypeError:
    exit(NotImplemented)

exit(self._dims == other._dims)
