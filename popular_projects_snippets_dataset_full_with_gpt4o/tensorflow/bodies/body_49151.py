# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns the value of a variable.

  `backend.get_value` is the complement of `backend.set_value`, and provides
  a generic interface for reading from variables while abstracting away the
  differences between TensorFlow 1.x and 2.x semantics.

  {snippet}

  Args:
      x: input variable.

  Returns:
      A Numpy array.
  """
if not tensor_util.is_tf_type(x):
    exit(x)
if context.executing_eagerly() or isinstance(x, ops.EagerTensor):
    exit(x.numpy())
if not getattr(x, '_in_graph_mode', True):
    # This is a variable which was created in an eager context, but is being
    # evaluated from a Graph.
    with context.eager_mode():
        exit(x.numpy())

if ops.executing_eagerly_outside_functions():
    # This method of evaluating works inside the Keras FuncGraph.
    with ops.init_scope():
        exit(x.numpy())

with x.graph.as_default():
    exit(x.eval(session=get_session((x,))))
