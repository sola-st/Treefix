# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns a `tf.TensorShape` that represents the shape of this tensor.

    In eager execution the shape is always fully-known.

    >>> a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    >>> print(a.shape)
    (2, 3)

    `tf.Tensor.get_shape()` is equivalent to `tf.Tensor.shape`.


    When executing in a `tf.function` or building a model using
    `tf.keras.Input`, `Tensor.shape` may return a partial shape (including
    `None` for unknown dimensions). See `tf.TensorShape` for more details.

    >>> inputs = tf.keras.Input(shape = [10])
    >>> # Unknown batch size
    >>> print(inputs.shape)
    (None, 10)

    The shape is computed using shape inference functions that are
    registered for each `tf.Operation`.

    The returned `tf.TensorShape` is determined at *build* time, without
    executing the underlying kernel. It is not a `tf.Tensor`. If you need a
    shape *tensor*, either convert the `tf.TensorShape` to a `tf.constant`, or
    use the `tf.shape(tensor)` function, which returns the tensor's shape at
    *execution* time.

    This is useful for debugging and providing early errors. For
    example, when tracing a `tf.function`, no ops are being executed, shapes
    may be unknown (See the [Concrete Functions
    Guide](https://www.tensorflow.org/guide/concrete_function) for details).

    >>> @tf.function
    ... def my_matmul(a, b):
    ...   result = a@b
    ...   # the `print` executes during tracing.
    ...   print("Result shape: ", result.shape)
    ...   return result

    The shape inference functions propagate shapes to the extent possible:

    >>> f = my_matmul.get_concrete_function(
    ...   tf.TensorSpec([None,3]),
    ...   tf.TensorSpec([3,5]))
    Result shape: (None, 5)

    Tracing may fail if a shape missmatch can be detected:

    >>> cf = my_matmul.get_concrete_function(
    ...   tf.TensorSpec([None,3]),
    ...   tf.TensorSpec([4,5]))
    Traceback (most recent call last):
    ...
    ValueError: Dimensions must be equal, but are 3 and 4 for 'matmul' (op:
    'MatMul') with input shapes: [?,3], [4,5].

    In some cases, the inferred shape may have unknown dimensions. If
    the caller has additional information about the values of these
    dimensions, `tf.ensure_shape` or `Tensor.set_shape()` can be used to augment
    the inferred shape.

    >>> @tf.function
    ... def my_fun(a):
    ...   a = tf.ensure_shape(a, [5, 5])
    ...   # the `print` executes during tracing.
    ...   print("Result shape: ", a.shape)
    ...   return a

    >>> cf = my_fun.get_concrete_function(
    ...   tf.TensorSpec([None, None]))
    Result shape: (5, 5)

    Returns:
      A `tf.TensorShape` representing the shape of this tensor.

    """
exit(self.shape)
