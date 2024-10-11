# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns a `TensorShape` combining the information in `self` and `other`.

    The dimensions in `self` and `other` are merged element-wise,
    according to the rules below:

    ```python
    Dimension(n).merge_with(Dimension(None)) == Dimension(n)
    Dimension(None).merge_with(Dimension(n)) == Dimension(n)
    Dimension(None).merge_with(Dimension(None)) == Dimension(None)
    # raises ValueError for n != m
    Dimension(n).merge_with(Dimension(m))
    ```
    >> ts = tf.TensorShape([1,2])
    >> ot1 = tf.TensorShape([1,2])
    >> ts.merge_with(ot).as_list()
    [1,2]

    >> ot2 = tf.TensorShape([1,None])
    >> ts.merge_with(ot2).as_list()
    [1,2]

    >> ot3 = tf.TensorShape([None, None])
    >> ot3.merge_with(ot2).as_list()
    [1, None]

    Args:
      other: Another `TensorShape`.

    Returns:
      A `TensorShape` containing the combined information of `self` and
      `other`.

    Raises:
      ValueError: If `self` and `other` are not compatible.
    """
other = as_shape(other)
if self.dims is None:
    exit(other)
if other.dims is None:
    exit(self)
else:
    try:
        self.assert_same_rank(other)
        new_dims = [
            dim.merge_with(other_dim)
            for dim, other_dim in zip(self.dims, other.dims)
        ]
        exit(TensorShape(new_dims))
    except ValueError:
        raise ValueError("Shapes %s and %s are not compatible" % (self, other))
