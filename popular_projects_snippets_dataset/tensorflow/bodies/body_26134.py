# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Maps `map_func` across the elements of this dataset.

    This transformation applies `map_func` to each element of this dataset, and
    returns a new dataset containing the transformed elements, in the same
    order as they appeared in the input. `map_func` can be used to change both
    the values and the structure of a dataset's elements. Supported structure
    constructs are documented
    [here](https://www.tensorflow.org/guide/data#dataset_structure).

    For example, `map` can be used for adding 1 to each element, or projecting a
    subset of element components.

    >>> dataset = Dataset.range(1, 6)  # ==> [ 1, 2, 3, 4, 5 ]
    >>> dataset = dataset.map(lambda x: x + 1)
    >>> list(dataset.as_numpy_iterator())
    [2, 3, 4, 5, 6]

    The input signature of `map_func` is determined by the structure of each
    element in this dataset.

    >>> dataset = Dataset.range(5)
    >>> # `map_func` takes a single argument of type `tf.Tensor` with the same
    >>> # shape and dtype.
    >>> result = dataset.map(lambda x: x + 1)

    >>> # Each element is a tuple containing two `tf.Tensor` objects.
    >>> elements = [(1, "foo"), (2, "bar"), (3, "baz")]
    >>> dataset = tf.data.Dataset.from_generator(
    ...     lambda: elements, (tf.int32, tf.string))
    >>> # `map_func` takes two arguments of type `tf.Tensor`. This function
    >>> # projects out just the first component.
    >>> result = dataset.map(lambda x_int, y_str: x_int)
    >>> list(result.as_numpy_iterator())
    [1, 2, 3]

    >>> # Each element is a dictionary mapping strings to `tf.Tensor` objects.
    >>> elements =  ([{"a": 1, "b": "foo"},
    ...               {"a": 2, "b": "bar"},
    ...               {"a": 3, "b": "baz"}])
    >>> dataset = tf.data.Dataset.from_generator(
    ...     lambda: elements, {"a": tf.int32, "b": tf.string})
    >>> # `map_func` takes a single argument of type `dict` with the same keys
    >>> # as the elements.
    >>> result = dataset.map(lambda d: str(d["a"]) + d["b"])

    The value or values returned by `map_func` determine the structure of each
    element in the returned dataset.

    >>> dataset = tf.data.Dataset.range(3)
    >>> # `map_func` returns two `tf.Tensor` objects.
    >>> def g(x):
    ...   return tf.constant(37.0), tf.constant(["Foo", "Bar", "Baz"])
    >>> result = dataset.map(g)
    >>> result.element_spec
    (TensorSpec(shape=(), dtype=tf.float32, name=None), TensorSpec(shape=(3,), \
dtype=tf.string, name=None))
    >>> # Python primitives, lists, and NumPy arrays are implicitly converted to
    >>> # `tf.Tensor`.
    >>> def h(x):
    ...   return 37.0, ["Foo", "Bar"], np.array([1.0, 2.0], dtype=np.float64)
    >>> result = dataset.map(h)
    >>> result.element_spec
    (TensorSpec(shape=(), dtype=tf.float32, name=None), TensorSpec(shape=(2,), \
dtype=tf.string, name=None), TensorSpec(shape=(2,), dtype=tf.float64, \
name=None))
    >>> # `map_func` can return nested structures.
    >>> def i(x):
    ...   return (37.0, [42, 16]), "foo"
    >>> result = dataset.map(i)
    >>> result.element_spec
    ((TensorSpec(shape=(), dtype=tf.float32, name=None),
      TensorSpec(shape=(2,), dtype=tf.int32, name=None)),
     TensorSpec(shape=(), dtype=tf.string, name=None))

    `map_func` can accept as arguments and return any type of dataset element.

    Note that irrespective of the context in which `map_func` is defined (eager
    vs. graph), tf.data traces the function and executes it as a graph. To use
    Python code inside of the function you have a few options:

    1) Rely on AutoGraph to convert Python code into an equivalent graph
    computation. The downside of this approach is that AutoGraph can convert
    some but not all Python code.

    2) Use `tf.py_function`, which allows you to write arbitrary Python code but
    will generally result in worse performance than 1). For example:

    >>> d = tf.data.Dataset.from_tensor_slices(['hello', 'world'])
    >>> # transform a string tensor to upper case string using a Python function
    >>> def upper_case_fn(t: tf.Tensor):
    ...   return t.numpy().decode('utf-8').upper()
    >>> d = d.map(lambda x: tf.py_function(func=upper_case_fn,
    ...           inp=[x], Tout=tf.string))
    >>> list(d.as_numpy_iterator())
    [b'HELLO', b'WORLD']

    3) Use `tf.numpy_function`, which also allows you to write arbitrary
    Python code. Note that `tf.py_function` accepts `tf.Tensor` whereas
    `tf.numpy_function` accepts numpy arrays and returns only numpy arrays.
    For example:

    >>> d = tf.data.Dataset.from_tensor_slices(['hello', 'world'])
    >>> def upper_case_fn(t: np.ndarray):
    ...   return t.decode('utf-8').upper()
    >>> d = d.map(lambda x: tf.numpy_function(func=upper_case_fn,
    ...           inp=[x], Tout=tf.string))
    >>> list(d.as_numpy_iterator())
    [b'HELLO', b'WORLD']

    Note that the use of `tf.numpy_function` and `tf.py_function`
    in general precludes the possibility of executing user-defined
    transformations in parallel (because of Python GIL).

    Performance can often be improved by setting `num_parallel_calls` so that
    `map` will use multiple threads to process elements. If deterministic order
    isn't required, it can also improve performance to set
    `deterministic=False`.

    >>> dataset = Dataset.range(1, 6)  # ==> [ 1, 2, 3, 4, 5 ]
    >>> dataset = dataset.map(lambda x: x + 1,
    ...     num_parallel_calls=tf.data.AUTOTUNE,
    ...     deterministic=False)

    The order of elements yielded by this transformation is deterministic if
    `deterministic=True`. If `map_func` contains stateful operations and
    `num_parallel_calls > 1`, the order in which that state is accessed is
    undefined, so the values of output elements may not be deterministic
    regardless of the `deterministic` flag value.

    Args:
      map_func: A function mapping a dataset element to another dataset element.
      num_parallel_calls: (Optional.) A `tf.int64` scalar `tf.Tensor`,
        representing the number elements to process asynchronously in parallel.
        If not specified, elements will be processed sequentially. If the value
        `tf.data.AUTOTUNE` is used, then the number of parallel
        calls is set dynamically based on available CPU.
      deterministic: (Optional.) When `num_parallel_calls` is specified, if this
        boolean is specified (`True` or `False`), it controls the order in which
        the transformation produces elements. If set to `False`, the
        transformation is allowed to yield elements out of order to trade
        determinism for performance. If not specified, the
        `tf.data.Options.deterministic` option (`True` by default) controls the
        behavior.
      name: (Optional.) A name for the tf.data operation.

    Returns:
      A new `Dataset` with the transformation applied as described above.
    """
# Loaded lazily due to a circular dependency (dataset_ops -> map_op ->
# dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import map_op
exit(map_op._map_v2(
    self,
    map_func,
    num_parallel_calls=num_parallel_calls,
    deterministic=deterministic,
    name=name))
