# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
"""Updates the `TensorShape` representing the shape of the dense tensor.

    With eager execution this operates as a shape assertion.
    Here the shapes match:

    >>> st = tf.SparseTensor(
    ...   indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
    >>> st.set_shape([3, 4])

    Passing a `None` in the new shape allows any value for that axis:

    >>> st.set_shape([3, None])

    An error is raised if an incompatible shape is passed.

    >>> st.set_shape([1, 4])
    Traceback (most recent call last):
    ...
    ValueError: Tensor's shape (3, 4) is not compatible with supplied
    shape [1, 4]

    When executing in a `tf.function`, or building a model using
    `tf.keras.Input`, `SparseTensor.set_shape` will *merge* the given `shape`
    with the current shape of this tensor, and set the tensor's shape to the
    merged value (see `tf.TensorShape.merge_with` for details):

    >>> st = tf.keras.Input(shape=[None, None, 3], sparse=True)
    >>> print(st.shape)
    (None, None, None, 3)

    Dimensions set to `None` are not updated:

    >>> st.set_shape([None, 224, 224, None])
    >>> print(st.shape)
    (None, 224, 224, 3)

    The main use case for this is to provide additional shape information
    that cannot be inferred from the graph alone.

    Caution: `set_shape` ensures that the applied shape is compatible with
    the existing shape, but it does not check at runtime. Setting
    incorrect shapes can result in inconsistencies between the
    statically-known graph and the runtime value of tensors.

    Args:
      shape: A `TensorShape` representing the shape of this tensor, a
        `TensorShapeProto`, a list, a tuple, or None.

    Raises:
      ValueError: If `shape` is not compatible with the current shape of
        this tensor.
    """
if not isinstance(shape, tensor_shape.TensorShape):
    shape = tensor_shape.TensorShape(shape)
self._dense_shape_default = self._dense_shape_default.merge_with(shape)
