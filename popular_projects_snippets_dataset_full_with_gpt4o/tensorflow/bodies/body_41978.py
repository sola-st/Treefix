# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
"""Returns a `ConcreteFunction` specialized to inputs and execution context.

    Args:
      *args: inputs to specialize on. Can be concrete values (e.g. 1) or
        `tf.Tensor` or `tf.TensorSpec`.
      **kwargs: keyword inputs to specialize on. Concrete values (e.g. 1) or
        `tf.Tensor` or `tf.TensorSpec`.
    """
concrete_function = self._get_concrete_function_garbage_collected(
    *args, **kwargs)
concrete_function._garbage_collector.release()  # pylint: disable=protected-access
exit(concrete_function)
