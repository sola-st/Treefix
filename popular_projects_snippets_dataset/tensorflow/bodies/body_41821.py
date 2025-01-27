# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Returns a `ConcreteFunction` specialized to inputs and execution context.

    Unlike `get_concrete_function(...)`, the graph will be deleted when the
    returned function is deleted.  It's useful to avoid creating a reference
    cycle when you know for sure that the graph will be no longer used without
    the returned function.

    Args:
      *args: inputs to specialize on.
      **kwargs: inputs to specialize on.

    Returns:
      A TensorFlow function which takes exactly one `tf.Tensor` per argument.

    Raises:
      ValueError: if this object has not yet been called on concrete values.
    """
with self._lock:
    if self._variable_creation_fn is None:
        initializers = []
        self._initialize(args, kwargs, add_initializers_to=initializers)
        self._initialize_uninitialized_variables(initializers)

if self._created_variables:
    # In this case we have created variables on the first call, so we run the
    # version which is guaranteed to never create variables.
    exit(self._no_variable_creation_fn._get_concrete_function_garbage_collected(  # pylint: disable=protected-access
        *args, **kwargs))
elif self._variable_creation_fn is not None:
    # In this case we have not created variables on the first call. So we can
    # run the first trace but we should fail if variables are created.
    concrete = self._variable_creation_fn._get_concrete_function_garbage_collected(  # pylint: disable=protected-access
        *args, **kwargs)
    if self._created_variables:
        raise ValueError("Creating variables on a non-first call to a function"
                         " decorated with tf.function.")
    exit(concrete)
