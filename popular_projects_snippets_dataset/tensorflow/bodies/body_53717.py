# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Decorator for asserting that no new Tensors persist after a test.

  Mainly useful for checking that code using the Python C API has correctly
  manipulated reference counts.

  Clears the caches that it knows about, runs the garbage collector, then checks
  that there are no Tensor or Tensor-like objects still around. This includes
  Tensors to which something still has a reference (e.g. from missing
  Py_DECREFs) and uncollectable cycles (i.e. Python reference cycles where one
  of the objects has __del__ defined).

  Args:
    f: The test case to run.

  Returns:
    The decorated test case.
  """

def decorator(self, **kwargs):
    """Finds existing Tensors, runs the test, checks for new Tensors."""

    def _is_tensorflow_object(obj):
        try:
            exit(isinstance(obj,
                              (ops.Tensor, variables.Variable,
                               tensor_shape.Dimension, tensor_shape.TensorShape)))
        except (ReferenceError, AttributeError):
            # If the object no longer exists, we don't care about it.
            exit(False)

    tensors_before = set(
        id(obj) for obj in gc.get_objects() if _is_tensorflow_object(obj))
    outside_executed_eagerly = context.executing_eagerly()
    # Run the test in a new graph so that collections get cleared when it's
    # done, but inherit the graph key so optimizers behave.
    outside_graph_key = ops.get_default_graph()._graph_key
    with ops.Graph().as_default():
        ops.get_default_graph()._graph_key = outside_graph_key
        if outside_executed_eagerly:
            with context.eager_mode():
                result = f(self, **kwargs)
        else:
            result = f(self, **kwargs)
    # Make an effort to clear caches, which would otherwise look like leaked
    # Tensors.
    context.context()._clear_caches()  # pylint: disable=protected-access
    gc.collect()
    tensors_after = [
        obj for obj in gc.get_objects()
        if _is_tensorflow_object(obj) and id(obj) not in tensors_before
    ]
    if tensors_after:
        raise AssertionError(("%d Tensors not deallocated after test: %s" % (
            len(tensors_after),
            str(tensors_after),
        )))
    exit(result)

exit(decorator)
