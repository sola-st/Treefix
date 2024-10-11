# Extracted from ./data/repos/tensorflow/tensorflow/python/types/core.py
"""Returns a `ConcreteFunction` specialized to input types.

    The arguments specified by `args` and `kwargs` follow normal function call
    rules. The returned `ConcreteFunction` has the same set of positional and
    keyword arguments as `self`, but their types are compatible to the types
    specified by `args` and `kwargs` (though not neccessarily equal).

    >>> @tf.function
    ... def f(x):
    ...   return x
    >>> f_concrete = f.get_concrete_function(tf.constant(1.0))
    >>> f_concrete = f.get_concrete_function(x=tf.constant(1.0))

    Unlike normal calls, `get_concrete_function` allow type specifiers instead
    of TensorFlow objects, so for example `tf.Tensor`s may be replaced with
    `tf.TensorSpec`s.

    >>> @tf.function
    ... def f(x):
    ...   return x
    >>> f_concrete = f.get_concrete_function(tf.TensorSpec([], tf.float64))

    If the function definition allows only one specialization, `args` and
    `kwargs` may be omitted altogether.

    >>> @tf.function(input_signature=[tf.TensorSpec(None, tf.float32)])
    ... def f(x):
    ...   return x
    >>> f_concrete = f.get_concrete_function()

    The returned `ConcreteFunction` can be called normally:

    >>> f_concrete(tf.constant(1.0))
    <tf.Tensor: shape=(), dtype=float32, numpy=1.0>
    >>> f_concrete(x=tf.constant(1.0))
    <tf.Tensor: shape=(), dtype=float32, numpy=1.0>

    Args:
      *args: inputs to specialize on.
      **kwargs: inputs to specialize on.

    Returns:
      A `ConcreteFunction`.
    """
pass
