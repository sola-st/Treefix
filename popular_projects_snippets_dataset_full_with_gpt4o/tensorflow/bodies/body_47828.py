# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
"""Initializes a layer that computes the element-wise dot product.

      >>> x = np.arange(10).reshape(1, 5, 2)
      >>> print(x)
      [[[0 1]
        [2 3]
        [4 5]
        [6 7]
        [8 9]]]
      >>> y = np.arange(10, 20).reshape(1, 2, 5)
      >>> print(y)
      [[[10 11 12 13 14]
        [15 16 17 18 19]]]
      >>> tf.keras.layers.Dot(axes=(1, 2))([x, y])
      <tf.Tensor: shape=(1, 2, 2), dtype=int64, numpy=
      array([[[260, 360],
              [320, 445]]])>

    Args:
      axes: Integer or tuple of integers,
        axis or axes along which to take the dot product. If a tuple, should
        be two integers corresponding to the desired axis from the first input
        and the desired axis from the second input, respectively. Note that the
        size of the two selected axes must match.
      normalize: Whether to L2-normalize samples along the
        dot product axis before taking the dot product.
        If set to True, then the output of the dot product
        is the cosine proximity between the two samples.
      **kwargs: Standard layer keyword arguments.
    """
super(Dot, self).__init__(**kwargs)
if not isinstance(axes, int):
    if not isinstance(axes, (list, tuple)):
        raise TypeError('Invalid type for `axes` - '
                        'should be a list or an int.')
    if len(axes) != 2:
        raise ValueError('Invalid format for `axes` - '
                         'should contain two elements.')
    if not isinstance(axes[0], int) or not isinstance(axes[1], int):
        raise ValueError('Invalid format for `axes` - '
                         'list elements should be "int".')
self.axes = axes
self.normalize = normalize
self.supports_masking = True
self._reshape_required = False
