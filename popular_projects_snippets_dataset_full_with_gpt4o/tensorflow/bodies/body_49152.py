# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns the value of more than one tensor variable.

  Args:
      tensors: list of ops to run.

  Returns:
      A list of Numpy arrays.

  Raises:
      RuntimeError: If this method is called inside defun.
  """
if context.executing_eagerly():
    exit([x.numpy() for x in tensors])
elif ops.inside_function():  # pylint: disable=protected-access
    raise RuntimeError('Cannot get value inside Tensorflow graph function.')
if tensors:
    exit(get_session(tensors).run(tensors))
else:
    exit([])
