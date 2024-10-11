# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Updates the shape of this tensor.

    Note: It is recommended to use `tf.ensure_shape` instead of
    `Tensor.set_shape`, because `tf.ensure_shape` provides better checking for
    programming errors and can create guarantees for compiler
    optimization.

    With eager execution this operates as a shape assertion.
    Here the shapes match:

    >>> t = tf.constant([[1,2,3]])
    >>> t.set_shape([1, 3])

    Passing a `None` in the new shape allows any value for that axis:

    >>> t.set_shape([1,None])

    An error is raised if an incompatible shape is passed.

    >>> t.set_shape([1,5])
    Traceback (most recent call last):
    ...
    ValueError: Tensor's shape (1, 3) is not compatible with supplied
    shape [1, 5]

    When executing in a `tf.function`, or building a model using
    `tf.keras.Input`, `Tensor.set_shape` will *merge* the given `shape` with
    the current shape of this tensor, and set the tensor's shape to the
    merged value (see `tf.TensorShape.merge_with` for details):

    >>> t = tf.keras.Input(shape=[None, None, 3])
    >>> print(t.shape)
    (None, None, None, 3)

    Dimensions set to `None` are not updated:

    >>> t.set_shape([None, 224, 224, None])
    >>> print(t.shape)
    (None, 224, 224, 3)

    The main use case for this is to provide additional shape information
    that cannot be inferred from the graph alone.

    For example if you know all the images in a dataset have shape [28,28,3] you
    can set it with `tf.set_shape`:

    >>> @tf.function
    ... def load_image(filename):
    ...   raw = tf.io.read_file(filename)
    ...   image = tf.image.decode_png(raw, channels=3)
    ...   # the `print` executes during tracing.
    ...   print("Initial shape: ", image.shape)
    ...   image.set_shape([28, 28, 3])
    ...   print("Final shape: ", image.shape)
    ...   return image

    Trace the function, see the [Concrete Functions
    Guide](https://www.tensorflow.org/guide/concrete_function) for details.

    >>> cf = load_image.get_concrete_function(
    ...     tf.TensorSpec([], dtype=tf.string))
    Initial shape:  (None, None, 3)
    Final shape: (28, 28, 3)

    Similarly the `tf.io.parse_tensor` function could return a tensor with
    any shape, even the `tf.rank` is unknown. If you know that all your
    serialized tensors will be 2d, set it with `set_shape`:

    >>> @tf.function
    ... def my_parse(string_tensor):
    ...   result = tf.io.parse_tensor(string_tensor, out_type=tf.float32)
    ...   # the `print` executes during tracing.
    ...   print("Initial shape: ", result.shape)
    ...   result.set_shape([None, None])
    ...   print("Final shape: ", result.shape)
    ...   return result

    Trace the function

    >>> concrete_parse = my_parse.get_concrete_function(
    ...     tf.TensorSpec([], dtype=tf.string))
    Initial shape:  <unknown>
    Final shape:  (None, None)

    Make sure it works:

    >>> t = tf.ones([5,3], dtype=tf.float32)
    >>> serialized = tf.io.serialize_tensor(t)
    >>> print(serialized.dtype)
    <dtype: 'string'>
    >>> print(serialized.shape)
    ()
    >>> t2 = concrete_parse(serialized)
    >>> print(t2.shape)
    (5, 3)

    Caution: `set_shape` ensures that the applied shape is compatible with
    the existing shape, but it does not check at runtime. Setting
    incorrect shapes can result in inconsistencies between the
    statically-known graph and the runtime value of tensors. For runtime
    validation of the shape, use `tf.ensure_shape` instead. It also modifies
    the `shape` of the tensor.

    >>> # Serialize a rank-3 tensor
    >>> t = tf.ones([5,5,5], dtype=tf.float32)
    >>> serialized = tf.io.serialize_tensor(t)
    >>> # The function still runs, even though it `set_shape([None,None])`
    >>> t2 = concrete_parse(serialized)
    >>> print(t2.shape)
    (5, 5, 5)

    Args:
      shape: A `TensorShape` representing the shape of this tensor, a
        `TensorShapeProto`, a list, a tuple, or None.

    Raises:
      ValueError: If `shape` is not compatible with the current shape of
        this tensor.
    """
# Reset cached shape.
self._shape_val = None

# We want set_shape to be reflected in the C API graph for when we run it.
if not isinstance(shape, tensor_shape.TensorShape):
    shape = tensor_shape.TensorShape(shape)
dim_list = []
if shape.dims is None:
    unknown_shape = True
else:
    unknown_shape = False
    for dim in shape.dims:
        if dim.value is None:
            dim_list.append(-1)
        else:
            dim_list.append(dim.value)
try:
    with self._op._graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
        pywrap_tf_session.TF_GraphSetTensorShape_wrapper(
            c_graph, self._as_tf_output(), dim_list, unknown_shape)
except errors.InvalidArgumentError as e:
    # Convert to ValueError for backwards compatibility.
    raise ValueError(e.message)
