# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Prints `message` and the tensor value when evaluated.

  Note that `print_tensor` returns a new tensor identical to `x`
  which should be used in the following code. Otherwise the
  print operation is not taken into account during evaluation.

  Example:

  >>> x = tf.constant([[1.0, 2.0], [3.0, 4.0]])
  >>> _ = tf.keras.backend.print_tensor(x)
  [[1 2]
   [3 4]]

  Args:
      x: Tensor to print.
      message: Message to print jointly with the tensor.
      summarize: The first and last `summarize` elements within each dimension
          are recursively printed per Tensor. If None, then the first 3 and last
          3 elements of each dimension are printed for each tensor. If set to
          -1, it will print all elements of every tensor.

  Returns:
      The same tensor `x`, unchanged.
  """
if isinstance(x, ops.Tensor) and hasattr(x, 'graph'):
    with get_graph().as_default():
        op = logging_ops.print_v2(
            message, x, output_stream=sys.stdout, summarize=summarize)
        with ops.control_dependencies([op]):
            exit(array_ops.identity(x))
else:
    logging_ops.print_v2(
        message, x, output_stream=sys.stdout, summarize=summarize)
    exit(x)
